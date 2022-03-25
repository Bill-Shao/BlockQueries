import numpy as np
from scipy.stats import norm
import csv

def stdev():
    with open('bitcoinity_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) #skip header
        vals = []

        for row in csv_reader:
            vals.append(float(row[1]))
        
        avg = sum(vals) / len(vals)
        sd = (sum([((x-avg)**2) for x in vals]) / len(vals)) ** 0.5
        return sd

with open('bitcoinity_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) #skip header
    minsinday = 60*24
    countMore = 0
    countTotal = 0
    total = []
    sd = stdev()
    for row in csv_reader:
        above = 1-norm(loc = float(row[1]), scale = sd).cdf(120)
        total.append(above)
        
        countTotal += minsinday/float(row[1])
        countMore += above*minsinday/float(row[1])
    print('Around ' + str(countMore) + ' blocks more than 2 hour difference.')
    print(str(countMore/countTotal) + ' fraction of 2hour/total blocks.')



#Values without distribution.
#Around 19.319922342293815 blocks more than 2 hour difference.
#3.094438379886008e-05 fraction of 2hour/total blocks.