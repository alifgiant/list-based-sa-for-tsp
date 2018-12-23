import matplotlib
from typing import List, Tuple

class City (object):
    def __init__(self, name: str, coordinate: List[float]):
        self.name = name
        self.coordinate = coordinate

    def __repr__(self):
        return f'name: {self.name}, coordinate: {self.coordinate}'

def evaluate_distance(a: City, b : City):
    pass

def read_data(file_location):
    with open(file_location) as file: # Use file to refer to the file object
        test_case_count = int(file.readline())
        test_case = list()
        for _ in range(test_case_count):
            names = file.readline().split()
            cities = list()
            for name in names:
                line = file.readline().split(',')
                coordinate = list(map(lambda x: float(x), line))
                cities.append(City(name, coordinate))
            optimal = float(file.readline())
            test_case.append((cities, optimal))
        
        return test_case
    return None

if __name__ == '__main__':
    DATA_FILE = "./data.in"
    DATA_SET = read_data(DATA_FILE)
    print(DATA_SET)
    pass