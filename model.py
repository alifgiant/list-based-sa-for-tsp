from typing import List, Callable

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
