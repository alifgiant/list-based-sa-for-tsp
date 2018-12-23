import matplotlib
import math
import os
import random
from typing import List, Tuple, Callable


class City (object):
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f'name: {self.name}, coordinate: {self.x},{self.y}'

class TestCase (object):
    def __init__(self, cities: List[City], optimal: float):
        self.cities = cities
        self.optimal = optimal

Solution = List[int]

def evaluate_distance(a: City, b : City) -> float:
    return math.sqrt(abs(a.x - b.x)**2 + abs(a.y - b.y)**2)

def evaluate_solution(cities: List[City], solution: Solution) -> float:
    solution_pair = zip(solution, solution[1:] + solution[:1])
    distances = [evaluate_distance(cities[a], cities[b]) for a, b in solution_pair]
    return sum(distances)

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

def generate_2_sorted_random(cities: List[City]) -> int:
    numbers = random.sample(range(len(cities)), 2)
    numbers.sort()
    return numbers

def inverse_solution(old_solution: Solution, i: int, j: int) -> Solution:
    return old_solution[:i] + old_solution[i:j][::-1] + old_solution[j:]

def insert_solution(old_solution: Solution, i: int, j: int) -> Solution:
    new_solution = old_solution[:]
    new_solution.insert(j, new_solution[i])
    new_solution.pop(i)
    return new_solution

def swap_solution(old_solution: Solution, i: int, j: int) -> Solution:
    new_solution = old_solution[:]
    temp = new_solution[i]
    new_solution[i] = new_solution[j]
    new_solution[j] = temp
    return new_solution

def create_new_solution(cities: List[City], old_solution: Solution) -> Solution:
    i, j = generate_2_sorted_random(cities)

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