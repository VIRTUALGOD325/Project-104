import csv
from collections import Counter

file = open("HeightWeight.csv","r")

reader = csv.reader(file)

file_data = list(reader)

file_data.pop(0)

height = []

def mean():
    for row in range(len(file_data)):
        num = file_data[row][1]
        height.append(float(num))

    total = 0

    for i in height:
        total += i

    mean = total/len(height)
    print(mean)

def median():
    for row in range(len(file_data)):
        num = file_data[row][1]
        height.append(float(num))

    n = len(height)
    height.sort()

    if n % 2 == 0:
        median1 = float(height[n//2])
        median2 = float(height[n//2-1])
        median = (median1 + median2)/2
    else:
        median = float(height[n//2])

    print(median)

def mode():
    for row in range(len(file_data)):
        num = file_data[row][1]
        height.append(float(num))

    data = Counter(height)

    mode_data_for_range = {

        "50-60":0,
        "60-70":0,
        "70-80":0
    }

    for height,occurence in data.items():
        if 50 < float(height) < 60:
            mode_data_for_range["50-60"] += occurence
        elif 60 <float(height) < 70:
            mode_data_for_range["60-70"] += occurence
        elif 70 <float(height) < 80:
            mode_data_for_range["70-80"] += occurence
        
    mode_range = 0
    mode_occurence = 0

    for range,occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_occurence = occurence
            mode_range = [int(range.split("-")[0]),int(range.split("-")[1])]

    mode = float((mode_range[0]+mode_range[1])/2)

    print(mode)

mean()
median()
mode()
