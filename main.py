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
    swap_opt = insert_solution(old_solution, i, j)

    evaluation = [evaluate_solution(cities, inverse_opt), evaluate_solution(cities, insert_opt), evaluate_solution(cities, swap_opt)]
    index = evaluation.index(min(evaluation))

    if index == 0:
        return inverse_opt
    elif index == 1:
        return insert_opt
    else:
        return swap_opt

def calculate_bad_result_acceptance_probability(tmax: float, evaluation_new_solution: float, evaluation_old_solution: float) -> float:
    return math.exp(-(evaluation_new_solution - evaluation_old_solution) / tmax)

"""
result should be look like this: [0, 1, 7, 9, 5, 4, 8, 6, 2, 3]
"""
def run_lbsa(testCase: TestCase, M: int = 100, K: int = 100, initial_T: float = 100) -> Solution:
    temparature_list = [initial_T]
    k = 0
    t = 0
    c = 0
    m = 0
    return [0,1,2,3]

if __name__ == '__main__':
    DATA_FILE = "./data.in"
    DATA_SET = read_data(DATA_FILE)
    
    test = DATA_SET[1]
    # print(run_lbsa(DATA_FILE[0]))