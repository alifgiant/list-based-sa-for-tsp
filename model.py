from typing import List, Callable


class Place (object):
    def __init__(self, name: str, travel_time: List[int], info: List[int]):
        self.name = name
        self.travel_time = travel_time
        self.info = info

    def __repr__(self):
        return f'name: {self.name}'


class TestCase (object):
    def __init__(self, cities: List[Place], optimal: float):
        self.places = cities
        self.optimal = optimal


Solution = List[int]
