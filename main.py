DATA_FILE = "./data.in"
DATA_SET = list()

class City (object):
    def __init__(self, names, distances, optimal):
        self.names = names
        self.distances = distances
        self.optimal = optimal

    def __repr__(self):
        return str(self.names)

with open(DATA_FILE) as file: # Use file to refer to the file object
    test_case_count = int(file.readline())
    for case in range(test_case_count):
        names = file.readline().split()
        distances = list()
        for name in names:
            distance = list(map(lambda x: float(x), file.readline().split()))
            distances.append(distance)
        optimal = float(file.readline())
        DATA_SET.append(City(names, distance, optimal))
    print(DATA_SET)