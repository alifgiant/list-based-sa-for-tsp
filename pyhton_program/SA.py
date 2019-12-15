import numpy as np
import random
import math
import collections
import pandas as pd
"""
import pymysql

def dbcheck():
  db = pymysql.connect("localhost","root","","crsgo_backend" )
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print ("Database version : %s " % data)
  db.close()
"""

#matriks jarak berdasarkan waktu
traveltime = [
    ['tangkuban perahu','tangkuban perahu', 0],
    ['tangkuban perahu','maribaya hot spring', 2816],
    ['tangkuban perahu','situ cuburuy', 6536],
    ['tangkuban perahu','observatorium bosscha', 3126],
    ['tangkuban perahu','gua sanghyang Tikoro', 9430],
    ['tangkuban perahu','stone garden geo park', 7725],
    ['tangkuban perahu','air terjun maribaya', 2893],
    ['tangkuban perahu','taman begonia', 2604],
    ['tangkuban perahu','taman hutan raya irhjuanda', 4185],
    ['tangkuban perahu','curug cimahi', 3926],
    ['maribaya hot spring','tangkuban perahu', 2812],
    ['maribaya hot spring','maribaya hot spring', 0],
    ['maribaya hot spring','situ cuburuy', 4157],
    ['maribaya hot spring','observatorium bosscha', 1757],
    ['maribaya hot spring','gua sanghyang Tikoro', 7065],
    ['maribaya hot spring','stone garden geo park', 5360],
    ['maribaya hot spring','air terjun maribaya', 77],
    ['maribaya hot spring','taman begonia', 633],
    ['maribaya hot spring','taman hutan raya irhjuanda', 1774],
    ['maribaya hot spring','curug cimahi', 2558],
    ['situ cuburuy','tangkuban perahu', 6395],
    ['situ cuburuy','maribaya hot spring', 4367],
    ['situ cuburuy','situ cuburuy', 0],
    ['situ cuburuy','observatorium bosscha', 4109],
    ['situ cuburuy','gua sanghyang Tikoro', 3025],
    ['situ cuburuy','stone garden geo park', 1320],
    ['situ cuburuy','air terjun maribaya', 4444],
    ['situ cuburuy','taman begonia', 4186],
    ['situ cuburuy','taman hutan raya irhjuanda', 3351],
    ['situ cuburuy','curug cimahi', 2565],
    ['observatorium bosscha','tangkuban perahu', 3020],
    ['observatorium bosscha','maribaya hot spring', 1705],
    ['observatorium bosscha','situ cuburuy', 3908],
    ['observatorium bosscha','observatorium bosscha', 0],
    ['observatorium bosscha','gua sanghyang tikoro', 6816],
    ['observatorium bosscha','stone garden geo park', 5111],
    ['observatorium bosscha','air terjun maribaya', 1782],
    ['observatorium bosscha','taman begonia', 1109],
    ['observatorium bosscha','taman hutan raya irhjuanda', 2690],
    ['observatorium bosscha','curug cimahi', 1454],
    ['gua sanghyang tikoro','tangkuban perahu', 9432],
    ['gua sanghyang tikoro','maribaya hot spring', 7404],
    ['gua sanghyang tikoro','situ cuburuy', 3320],
    ['gua sanghyang tikoro','observatorium bosscha', 7146],
    ['gua sanghyang tikoro','gua sanghyang Tikoro', 0],
    ['gua sanghyang tikoro','stone garden geo park', 2540],
    ['gua sanghyang tikoro','air terjun maribaya', 7481],
    ['gua sanghyang tikoro','taman begonia', 7223],
    ['gua sanghyang tikoro','taman hutan raya irhjuanda', 6388],
    ['gua sanghyang tikoro','curug cimahi', 5602],
    ['stone garden geo park','tangkuban perahu', 7391],
    ['stone garden geo park','maribaya hot spring', 5363],
    ['stone garden geo park','situ cuburuy', 1279],
    ['stone garden geo park','observatorium bosscha', 5104],
    ['stone garden geo park','gua sanghyang Tikoro', 3008],
    ['stone garden geo park','stone garden geo park', 0],
    ['stone garden geo park','air terjun maribaya', 5439],
    ['stone garden geo park','taman begonia', 5181],
    ['stone garden geo park','taman hutan raya irhjuanda', 4347],
    ['stone garden geo park','curug cimahi', 3501],
    ['air terjun maribaya','tangkuban perahu', 2888],
    ['air terjun maribaya','maribaya hot spring', 77],
    ['air terjun maribaya','situ cuburuy', 4234],
    ['air terjun maribaya','observatorium bosscha', 1834],
    ['air terjun maribaya','gua sanghyang Tikoro', 7142],
    ['air terjun maribaya','stone garden geo park', 5437],
    ['air terjun maribaya','air terjun maribaya', 0],
    ['air terjun maribaya','taman begonia', 709],
    ['air terjun maribaya','taman hutan raya irhjuanda', 1851],
    ['air terjun maribaya','curug cimahi', 2635],
    ['taman begonia','tangkuban perahu', 2752],
    ['taman begonia','maribaya hot spring', 596],
    ['taman begonia','situ cuburuy', 3964],
    ['taman begonia','observatorium bosscha', 1125],
    ['taman begonia','gua sanghyang Tikoro', 6872],
    ['taman begonia','stone garden geo park', 5167],
    ['taman begonia','air terjun maribaya', 673],
    ['taman begonia','taman begonia', 0],
    ['taman begonia','taman hutan raya irhjuanda', 1581],
    ['taman begonia','curug cimahi', 1925],
    ['taman hutan raya irhjuanda','tangkuban perahu', 4549],
    ['taman hutan raya irhjuanda','maribaya hot spring', 1978],
    ['taman hutan raya irhjuanda','situ cuburuy', 3121],
    ['taman hutan raya irhjuanda','observatorium bosscha', 2921],
    ['taman hutan raya irhjuanda','gua sanghyang Tikoro', 6029],
    ['taman hutan raya irhjuanda','stone garden geo park', 4324],
    ['taman hutan raya irhjuanda','air terjun maribaya', 2055],
    ['taman hutan raya irhjuanda','taman begonia', 1797],
    ['taman hutan raya irhjuanda','taman hutan raya irhjuanda', 0],
    ['taman hutan raya irhjuanda','curug cimahi', 3380],
    ['curug cimahi','tangkuban perahu', 3830],
    ['curug cimahi','maribaya hot spring', 2516],
    ['curug cimahi','situ cuburuy', 2641],
    ['curug cimahi','observatorium bosscha', 1544],
    ['curug cimahi','gua sanghyang Tikoro', 5503],
    ['curug cimahi','stone garden geo park', 3798],
    ['curug cimahi','air terjun maribaya', 2593],
    ['curug cimahi','taman begonia', 1920],
    ['curug cimahi','taman hutan raya irhjuanda',3174],
    ['curug cimahi','curug cimahi', 0],
]

#[hotel, destinasi tujuan, waktu tempuh hotel ke destinasi(detik), waktu tempuh destinasi ke hotel(detik)]
hotel = [
    ['reddorz natuna','tangkuban perahu', 5246, 5144],
    ['reddorz natuna','maribaya hot spring', 2651, 2732],
    ['reddorz natuna','situ cuburuy', 2524, 2886],
    ['reddorz natuna','observatorium bosscha', 2900, 2936],
    ['reddorz natuna','gua sanghyang tikoro', 5434, 5930],
    ['reddorz natuna','stone garden geo park', 3777, 3913],
    ['reddorz natuna','air terjun maribaya', 2727, 2809],
    ['reddorz natuna','taman begonia', 2468, 2536],
    ['reddorz natuna','taman hutan raya irhjuanda', 1705, 1768],
    ['reddorz natuna','curug cimahi', 3119, 3110],
]

#tempat destinasi
#['destinasi', 'tarif', 'rating', 'durasi', 'open_time', 'close_time']
dest = [
    ['tangkuban perahu',20000,3.5,7200,8,17],
    ['maribaya hot spring',35000,4,10800,8,10],
    ['situ cuburuy',20000,3,0,0,24],
    ['observatorium bosscha',15000,4,0,7,19],
    ['gua sanghyang tikoro',0,0,0,0,24],
    ['stone garden geo park',3000,3.5,7200,0,24],
    ['air terjun maribaya',7500,4,0,8,18],
    ['taman begonia',10000,4,10800,7,17],
    ['taman hutan raya irhjuanda',11000,4,7200,0,24],
    ['curug cimahi',12000,4,3600,0,24],
]

w1 = 0.5
w2 = 0.3
w3 = 0.2

def evaluate(destinasi):
    dist = 0
    rating = 0
    tarif = 0
    a = destinasi[0][0]
    for index in range(len(hotel)):
      if hotel[index][1] == a:
         dist += float(hotel[index][2])
         break
    #print(hotel[index][0], hotel[index][1], dist)     
    for index in range(len(destinasi)):
        rating += float(destinasi[index][2])
        tarif  += float(destinasi[index][1])
        a = destinasi[index][0]        
        if index == len(destinasi) - 1:
          for m in range(len(hotel)):
            if hotel[m][1] == destinasi[index][0]:
               break
          b = hotel[m][3]
        else:
          b = destinasi[index + 1][0]
        for m in range(len(traveltime)):
           if traveltime[m][0] == a and traveltime[m][1] == b:
              #print(traveltime[m][0], traveltime[m][1], traveltime[m][2])
              dist += float(traveltime[m][2])
              break              

    for index in range(len(hotel)):
      if hotel[index][1] == a:
         #print(hotel[index][1], hotel[index][0], hotel[index][2])
         dist += float(hotel[index][2])
         break
    #Bagian perhitungan list-based SA berdasarkan Tarif, Rating, dan Waktu Buka Tutup
    energy = ( w1 * dist + w2 * rating / len(destinasi) + w3 * tarif / len(destinasi)) / 3.0
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

def process(destinasi, temperature = 400, cooling_factor = .001):
    current = evaluate(destinasi)
    #print(current)
    
    while temperature > 0.001:
        new_solution = swap(destinasi)
        energy = evaluate(new_solution)        
        if accept_solution(current, energy, temperature):
            destinasi = new_solution
            current = energy        
        temperature *= 1 - cooling_factor

    return destinasi


destinasi = process(dest, temperature = 400)    
print(destinasi)

daySolution = []
mdest = np.copy(destinasi)

for dayCount in range(3):
   finishedTime = 0
   arrivalTime = 0
   currentNode = mdest[0][0]      
   mhotel = None
   for index in range(len(hotel)):
     if hotel[index][1] == currentNode:
        #print(hotel[index][1], hotel[index][0], hotel[index][2])
        finishedTime = float(hotel[index][2])/3600
        mhotel = hotel[index][0]
        break      
   #print(dayCount, mhotel, currentNode, finishedTime)
   daySolution.append([dayCount, currentNode])
   dayRemain = []
   for index in range(1,len(mdest)):
       a = mdest[index][0]
       durasi = 0
       for m in range(len(traveltime)):
          if traveltime[m][0] == currentNode and traveltime[m][1] == a:
             durasi = float(traveltime[m][2])/3600
             #print(traveltime[m][0], traveltime[m][1], traveltime[m][2]/3600)          
             break        

       arrivalTime = finishedTime + durasi
       finishedTime = arrivalTime + float(mdest[index][3]) / 3600
       #print(a, arrivalTime, finishedTime, float(mdest[index][4]), float(mdest[index][5]))
       if arrivalTime >= float(mdest[index][4]) and arrivalTime <= float(mdest[index][5]):
          daySolution.append([dayCount, mdest[index][0]])
          currentNode = mdest[index][0]
          #print(currentNode)
       else:
          dayRemain.append(mdest[index])   
   mdest = np.copy(dayRemain)       

#Print Daftar lokasi yang dikunjungi       
for index in range(len(daySolution)):
   print("Hari #{} {}".format(daySolution[index][0]+1, daySolution[index][1]))

#Print Total Biaya Perjalanan 
columns_new = ['destinasi', 'tarif', 'rating', 'durasi', 'open_time', 'close_time']
df_destinasi = pd.DataFrame(destinasi, columns=columns_new)
total_biaya = pd.to_numeric(df_destinasi['tarif'])
print('\nRekap Perjalanan')
print('Total Biaya Selama Perjalanan =  Rp.',total_biaya.sum())

