import matplotlib
import math
import os
import random
from typing import List, Callable, Tuple
from model import *
from config import M, K, INIT_P, T_LENGTH, SHOW_VISUAL, is_debug
import data


def evaluate_distance(a: Place, b: Place) -> float:
    dest_index = data.dest_name.index(b.name)
    time = a.travel_time[dest_index] / 9999
    tarif = a.info[0] / 99999
    rating = (a.info[1] / 5) * -1
    return abs((time + tarif + rating) * 1000)


def is_solution_valid(places: List[Place]) -> bool:
    return True


def evaluate_solution(places: List[Place], solution: Solution) -> float:
    solution_pair = zip(solution, solution[1:] + solution[:1])
    distances = [evaluate_distance(places[a], places[b])
                 for a, b in solution_pair]
    total = sum(distances)
    return total


def read_data(location_names: List[str], location_travel: List[int], location_info: List[int]) -> List[TestCase]:
    places = list()
    for i in range(len(location_names)):
        places.append(
            Place(location_names[i], location_travel[i], location_info[i]))

    return [TestCase(places, 1)]


def generate_2_random_index(places: List[Place]) -> int:
    return random.sample(range(1,len(places)), 2)


def generate_random_probability_r() -> float:
    return random.uniform(0.00000001, 1)


"""
given 
index [i, j] = [3, 6]
a list    = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
will return [0, 1, 2, 5, 4, 3, 6, 7, 8, 9]
"""


def inverse_solution(old_solution: Solution, places: List[Place], i: int = -1, j: int = -1) -> Solution:
    if i == -1 or j == -1:
        i, j = generate_2_random_index(places)
    numbers = [i, j]
    numbers.sort()
    i, j = numbers
    return old_solution[:i] + old_solution[i:j][::-1] + old_solution[j:]


"""
given 
index [i, j] = [3, 6]
a list    = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
will return [0, 1, 2, 4, 5, 3, 6, 7, 8, 9]
"""


def insert_solution(old_solution: Solution, places: List[Place], i: int = -1, j: int = -1) -> Solution:
    if i == -1 or j == -1:
        i, j = generate_2_random_index(places)

    new_solution = old_solution[:]
    new_solution.insert(j, new_solution[i])
    if j < i:
        i += 1  # because have inserted, the list is shifted by 1
    new_solution.pop(i)
    return new_solution


"""
given 
index [i, j] = [3, 6]
a list    = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
will return [0, 1, 2, 6, 4, 5, 3, 7, 8, 9]
"""


def swap_solution(old_solution: Solution, places: List[Place], i: int = -1, j: int = -1) -> Solution:
    if i == -1 or j == -1:
        i, j = generate_2_random_index(places)

    new_solution = old_solution[:]
    temp = new_solution[i]
    new_solution[i] = new_solution[j]
    new_solution[j] = temp
    return new_solution


def create_new_solution(places: List[Place], old_solution: Solution) -> Solution:
    inverse_opt = inverse_solution(old_solution, places)
    while not is_solution_valid(inverse_opt):
        inverse_opt = inverse_solution(old_solution, places)

    insert_opt = insert_solution(old_solution, places)
    while not is_solution_valid(insert_opt):
        insert_opt = insert_solution(old_solution, places)

    swap_opt = swap_solution(old_solution, places)
    while not is_solution_valid(swap_opt):
        swap_opt = swap_solution(old_solution, places)

    evaluation = [
        evaluate_solution(places, inverse_opt),
        evaluate_solution(places, insert_opt),
        evaluate_solution(places, swap_opt)
    ]
    index = evaluation.index(min(evaluation))

    if index == 0:
        return inverse_opt
    elif index == 1:
        return insert_opt
    else:
        return swap_opt


def calculate_bad_result_acceptance_probability(tmax: float, evaluation_new_solution: float, evaluation_old_solution: float) -> float:
    return math.exp(-(evaluation_new_solution - evaluation_old_solution) / tmax)


def calculate_new_temparature(r_probability: float, old_temparature: float, evaluation_new_solution: float, evaluation_old_solution: float) -> float:
    return (old_temparature - (evaluation_new_solution - evaluation_old_solution)) / math.log(r_probability)


"""
create initial temparature
temparature_list_length is how many try we find the initial temp
initial_acc_probability should be 0..1
"""


def create_initial_temp(places: List[Place], temparature_list_length: int, initial_acc_probability: float) -> List[float]:
    solution = list(range(len(places)))
    temparature_list = [2]

    for _ in range(temparature_list_length):
        old_solution = solution
        new_solution = create_new_solution(places, solution)

        new_evaluation = evaluate_solution(places, new_solution)
        old_evaluation = evaluate_solution(places, old_solution)

        if new_evaluation < old_evaluation:
            solution = new_solution

        t = (- abs(new_evaluation - old_evaluation)) / \
            math.log(initial_acc_probability)
        temparature_list.append(t)

    return temparature_list


"""
result should be look like this: [0, 1, 7, 9, 5, 4, 8, 6, 2, 3]
"""


def run_lbsa(places: List[Place], M: int, K: int, temparature_list_length: int, initial_acc_probability: float, is_debug: bool = False) -> Tuple[Solution, List[float]]:
    temparature_list = create_initial_temp(
        places, temparature_list_length, initial_acc_probability)
    temparature_list = [max(temparature_list)]
    solution = list(range(len(places)))
    evaluation_result_list = list()  # debugging purpose

    k = 0
    while k <= K:
        # clean temparature list
        k += 1
        t = 0
        m = 0
        c = 0

        while m <= M:
            m += 1
            old_solution = solution
            new_solution = create_new_solution(places, old_solution)

            new_evaluation = evaluate_solution(places, new_solution)
            old_evaluation = evaluate_solution(places, old_solution)
            is_new_picked = False

            if new_evaluation < old_evaluation:
                solution = new_solution
                is_new_picked = True

            else:
                p = calculate_bad_result_acceptance_probability(
                    max(temparature_list), new_evaluation, old_evaluation)
                r = generate_random_probability_r()

                if r > p:
                    t = calculate_new_temparature(
                        r, t, new_evaluation, old_evaluation)
                    temparature_list.append(t)
                    solution = new_solution
                    is_new_picked = True
                    c += 1

            if is_debug:
                if is_new_picked:
                    print(m, k, new_solution, new_evaluation)
                else:
                    print(m, k, old_solution, old_evaluation)

            if is_new_picked:
                evaluation_result_list.append(new_evaluation)
            else:
                evaluation_result_list.append(old_evaluation)

        if c > 0:
            t = t/c
            temparature_list.remove(max(temparature_list))
            temparature_list.append(t/c)

    return solution, evaluation_result_list


if __name__ == '__main__':
    DATA_SET = read_data(data.dest_name, data.time_travel, data.info)

    for test in DATA_SET:
        solution, result_list = run_lbsa(
            test.places, M, K, T_LENGTH, INIT_P, is_debug)
        print('solution:', solution, 'fitness:',
              evaluate_solution(test.places, solution))

        if SHOW_VISUAL:
            import matplotlib.pyplot as plt
            # for Place in test.places:
            #     plt.plot(Place.x, Place.y, color='r', marker='o')

            # solution.append(solution[0])
            # x_points = [test.places[i].x for i in solution]
            # y_points = [test.places[i].y for i in solution]

            # plt.plot(x_points, y_points, linestyle='--', color='b')
            # plt.show()  # path visualization

            plt.plot(list(range(len(result_list))),
                     result_list, linestyle='-', color='b')
            plt.show()  # graph visualization
