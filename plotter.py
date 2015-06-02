import matplotlib.pyplot as plt
import csv

datafile = open('results.csv', 'r')
datareader = csv.reader(datafile)
percs = []

dealerfile = open('resultsDealer.csv', 'r')
dealerreader = csv.reader(dealerfile)
dealerpercs = []

randomfile = open('resultsRandom.csv', 'r')
randomreader = csv.reader(randomfile)
randompercs = []

data = []

for line in datareader:
	data.append(line)
	percs.append(line[-1])

for line in dealerreader:
	dealerpercs.append(line[-1])

for line in randomreader:
	randompercs.append(line[-1])

finalqs = data[-1][0]

for line in finalqs.split():
	print(line)

fig = plt.figure(figsize=(6, 3.5))
plt.xlabel("Trial Number")
plt.ylabel("Win Percentage")
plt.title("Blackjack Win Percentage vs. Time")

plt.plot(percs, label="Q-Learning")
plt.plot(dealerpercs, label="Dealer Strategy")
plt.plot(randompercs, label="Random Strategy")

plt.legend(loc='lower right', frameon=False, numpoints=1)
plt.show()
