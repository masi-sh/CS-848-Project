import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
import csv
import random
from random import *


with open('outds.csv', 'w') as csvfile:
	fieldnames = ['ID', 'Salary(K)', 'Neighborhood', 'Jobtitle']
	outdswriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
	Neighborhood = ['Westmount','Westmount', 'Westmount','Westmount', 'Beechwood', 'Beechwood', 'Beechwood', 'Lakeshore', 'Lakeshore']
	Jobtitle = ['Eng', 'Eng', 'Dr', 'Dr', 'Lawyer']

	outdswriter.writeheader()
	for x in range(1, 90000):
		outdswriter.writerow({'ID': x, 'Salary(K)': randint(300, 500), 'Neighborhood': choice(Neighborhood), 'Jobtitle': choice(Jobtitle)})

	for x in range (90000, 100000):	    
		outdswriter.writerow({'ID': x, 'Salary(K)': randint(700, 800), 'Neighborhood': choice(Neighborhood), 'Jobtitle': choice(Jobtitle)})


