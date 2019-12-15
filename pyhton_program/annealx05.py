import numpy as np
import matplotlib.pyplot as plt
import random
import math
import collections

# [destinasi, (lot,lan), tarif, rating, durasi, open, close]    
    
cities = [
    ['Hotel',(40.72, 74.00),0, 5, 0, 0, 24],
    ['New York City',(40.72, 74.00),0, 5, 0, 0, 24],
    ['Los Angeles',(34.05, 118.25),10, 5, 2, 8, 20],
    ['Chicago',(41.88, 87.63),10, 5, 2, 8, 20],
    ['Houston',(29.77, 95.38),15, 5, 2, 8, 20],
    ['Phoenix',(33.45, 112.07),13, 5, 2, 8, 20],
    ['Philadelphia',(39.95, 75.17),12, 5, 2, 8, 20],
    ['San Antonio',(29.53, 98.47),10, 5, 2, 8, 20],
    ['Dallas',(32.78, 96.80),10, 5, 2, 8, 20],
    ['San Diego',(32.78, 117.15),10, 5, 2, 8, 20],
    ['San Jose',(37.30, 121.87),5, 5, 2, 8, 20],
    ['Detroit',(42.33, 83.05),5, 5, 2, 8, 20],
    ['San Francisco',(37.78, 122.42),8, 5, 2, 8, 20],
    ['Jacksonville',(30.32, 81.70),8, 5, 2, 8, 20],
    ['Indianapolis',(39.78, 86.15),8, 5, 2, 8, 20],
    ['Austin',(30.27, 97.77),3, 5, 2, 8, 20],
    ['Columbus',(39.98, 82.98),3, 5, 2, 8, 20],
    ['Fort Worth',(32.75, 97.33),3, 5, 2, 8, 20],
    ['Charlotte',(35.23, 80.85),4, 5, 2, 8, 20],
    ['Memphis',(35.12, 89.97),5, 5, 2, 8, 20],
    ['Baltimore',(39.28, 76.62),10, 5, 2, 8, 20]
]

hotel = [['Hotel',(40.72, 74.00)]]
w1 = 0.5
w2 = 0.3
w3 = 0.2

def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 3963  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R

# [destinasi, (lot,lan), tarif, rating, durasi, open, close]    
                    
def evaluate(cities):
    dist = 0
    rating = 0
    tarif = 0
    for index in range(len(cities)):
        rating += cities[index][3]
        tarif  += cities[index][2]
        a = cities[index][1]
        if index == len(cities) - 1:
            b = cities[0][1]
        else:
            b = cities[index + 1][1]
        dist += np.linalg.norm(np.array(a)-np.array(b))
        #dist += distance(a, b) 
        #index += 1
    dist += np.linalg.norm(np.array(hotel[0][1])-np.array(a))
    energy = ( w1 * dist + w2 * rating + w3 * tarif ) / 3.0
    return energy

def swap(x):
    i = random.randint(0, len(x) - 2)
    j = random.randint(i, len(x) - 1)

    y = np.copy(x)
    y[i: j] = y[i: j][::-1]

    return y


def accept_solution(energy1, energy2, temperature):
    if energy1 > energy2:
        return True
    else:
        a = math.exp((energy1 - energy2) / temperature)
        b = random.random()
        if a > b:
            return True
        else:
            return False

def process(cities, temperature = 400, cooling_factor = .001):
    current = evaluate(cities)
    print(current)
    
    while temperature > 0.001:
        new_solution = swap(cities)
        energy = evaluate(new_solution)
        if accept_solution(current, energy, temperature):
            cities = new_solution
            current = energy
        print(energy)
        temperature *= 1 - cooling_factor

    return cities

cities = process(cities, temperature = 400)
while cities[0][0] != 'Hotel':
   d = collections.deque(cities)
   d.rotate(1)
   cities = d
#print(cities)

# [destinasi, (lot,lat), tarif, rating, durasi, open, close]    

dayCount = 1
daySolution = []

del cities[0]   # delete Hotel
print(cities)
currentNode = cities[0][1]  # (lot, lat)
currentNodes = cities[0]

del cities[0]   # delete New York

finishedTime = 0
arrivalTime = 0

for index in range(len(cities)):
    a = cities[index][1]
    print(currentNodes, cities[index])
    arrivalTime = finishedTime + np.linalg.norm(np.array(a)-np.array(currentNode))
    finishedTime = arrivalTime + cities[index][4]
    if arrivalTime >= cities[index][5] and arrivalTime <= cities[index][6]:
       daySolution.append([dayCount, cities[index]])
       currentNode = cities[index][1]
       currentNodes = cities[index]
dayCount += 1
print(daySolution)

"""
plt.plot(cities[:][0], cities[:][1], color='red', zorder=0)
plt.scatter(cities[:][0], cities[:][1], marker='o')
plt.axis('off')
plt.show()
"""