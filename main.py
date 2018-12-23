import matplotlib
import math
from typing import List, Tuple

class City (object):
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f'name: {self.name}, coordinate: {self.x},{self.y}'

def evaluate_distance(a: City, b : City) -> float:
    return math.sqrt(abs(a.x - b.x) + abs(a.y - b.y))

def read_data(file_location):
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
            test_case.append((cities, optimal))
        
        return test_case
    return None

if __name__ == '__main__':
    DATA_FILE = "./data.in"
    DATA_SET = read_data(DATA_FILE)
    print(DATA_SET)
    pass