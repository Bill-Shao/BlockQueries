import numpy as np
from scipy.stats import poisson
import csv

with open('bitcoinity_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) #skip header
    minsinday = 60*24
    countMore = 0
    countTotal = 0
    blocknum = 0
    for row in csv_reader:
    
        blocknum+=1
        above = 1-poisson.cdf(120, float(row[1]))
        
        countTotal += minsinday/float(row[1])
        countMore += above*minsinday/float(row[1])
    print('Around ' + str(countMore) + ' blocks more than 2 hour difference.')
    print(str(countMore/countTotal) + ' fraction of 2hour/total blocks.')

