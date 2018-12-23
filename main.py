import matplotlib
import math
import os
import random
from typing import List, Callable

from model import *


def evaluate_distance(a: City, b : City) -> float:
    return math.sqrt(abs(a.x - b.x)**2 + abs(a.y - b.y)**2)

def evaluate_solution(cities: List[City], solution: Solution, is_fitness_calculation: bool = True) -> float:
    solution_pair = zip(solution, solution[1:] + solution[:1])
    distances = [evaluate_distance(cities[a], cities[b]) for a, b in solution_pair]
    total = sum(distances)
    return total if not is_fitness_calculation else -total

def read_data(file_location: str) -> List[TestCase]:
    if os.path.isfile(file_location):
        with open(file_location) as file: # Use file to refer to the file object
            test_case_count = int(file.readline())
            test_case = list()
            for _ in range(test_case_count):
                names = file.readline().split()
                cities = list()
                for name in names:
                    line = file.readline().split(',')
                    x, y = list(map(lambda x: float(x), line))
                    cities.append(City(name, x, y))
                optimal = float(file.readline())
                test_case.append(TestCase(cities, optimal))
            
        return test_case
    return list()

def generate_2_random_index(cities: List[City]) -> int:
    return random.sample(range(len(cities)), 2)

def generate_random_probability_r() -> float:
    return random.uniform(0, 1)

"""
given 
index [i, j] = [3, 6]
a list    = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
will return [0, 1, 2, 5, 4, 3, 6, 7, 8, 9]
"""
def inverse_solution(old_solution: Solution, i: int, j: int) -> Solution:
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
def insert_solution(old_solution: Solution, i: int, j: int) -> Solution:
    new_solution = old_solution[:]
    new_solution.insert(j, new_solution[i])
    if j < i:
        i += 1 # because have inserted, the list is shifted by 1
    new_solution.pop(i)
    return new_solution

"""
given 
index [i, j] = [3, 6]
a list    = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
will return [0, 1, 2, 6, 4, 5, 3, 7, 8, 9]
"""
def swap_solution(old_solution: Solution, i: int, j: int) -> Solution:
    new_solution = old_solution[:]
    temp = new_solution[i]
    new_solution[i] = new_solution[j]
    new_solution[j] = temp
    return new_solution

def create_new_solution(cities: List[City], old_solution: Solution, i_test: int = -1, j_test: int = -1) -> Solution:
    # helper for unit test, so number is not random
    i, j = i_test, j_test 

    if i == -1 or j == -1:
        i, j = generate_2_random_index(cities)

    inverse_opt = inverse_solution(old_solution, i, j)
    insert_opt = insert_solution(old_solution, i, j)
    swap_opt = swap_solution(old_solution, i, j)

    evaluation = [evaluate_solution(cities, inverse_opt, False), evaluate_solution(cities, insert_opt, False), evaluate_solution(cities, swap_opt, False)]
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
result should be look like this: [0, 1, 7, 9, 5, 4, 8, 6, 2, 3]
"""
def run_lbsa(cities: List[City], M: int = 100, K: int = 100, initial_T: float = 100) -> Solution:
    temparature_list = [initial_T]
    solution = list(range(len(cities)))

    k = 0
    while k <= K:
        # clean temparature list
        # temparature_list = list(filter(lambda a: a != 0.0, temparature_list))
        k += 1
        t = 0
        m = 0
        c = 0

        while m <= M:
            m += 1
            new_solution = create_new_solution(cities, solution)

            new_evaluation = evaluate_solution(cities, new_solution)
            old_evaluation = evaluate_solution(cities, solution)

            if  new_evaluation < old_evaluation:
                solution = new_solution
            else:
                p = calculate_bad_result_acceptance_probability(max(temparature_list), new_evaluation, old_evaluation)
                r = generate_random_probability_r()

                if r < p:
                    t = calculate_new_temparature(r, t, new_evaluation, old_evaluation)
                    if t != 0.0:
                        temparature_list.append(t)
                    solution = new_solution
                    c += 1
        
        if c > 0:
            t = t/c
            if t != 0.0:
                temparature_list.remove(max(temparature_list))
                temparature_list.append(t/c)

    return solution

if __name__ == '__main__':
    DATA_FILE = "./data.in"
    DATA_SET = read_data(DATA_FILE)

    for test in DATA_SET:
        solution = run_lbsa(test.cities, 10, 10, 100)
        print(solution)