import matplotlib.pyplot as plt
import csv

datafile = open('results.csv', 'r')
datareader = csv.reader(datafile)
percs = []

for line in datareader:
	percs.append(line[-1])

plt.plot(percs)
plt.show()
