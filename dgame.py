from deck import *
from Card import *
from bjutils import *
from player import *
from dealer import *
from qlearn import *
import csv
import time

global Q_old

def game(qdict, trial, wins):
	q = Qlearn()
	p = Player()
	d = Dealer()
	d.deal(p)
	status = 2
	epsilon = 0.05
	#print("starting a game...")
	#time.sleep(1)
	while status == 2:
		#print(valHand(p.hand))
		if valHand(p.hand) < 18:
			status = d.playRound(p, "HIT")
		else:
			status = d.playRound(p, "STAND")
		if status == 1:
			wins += 1
	return qdict, wins

if __name__ == "__main__":
	#Q1 = 0.5
	#Q2 = 0.5
	trial = 1
	wins = 0
	qdict = {
		4 : [0.5, 0.5, 0.5, 0.5],
		5 : [0.5, 0.5, 0.5, 0.5],
		6 : [0.5, 0.5, 0.5, 0.5],
		7 : [0.5, 0.5, 0.5, 0.5],
		8 : [0.5, 0.5, 0.5, 0.5],
		9 : [0.5, 0.5, 0.5, 0.5],
		10 : [0.5, 0.5, 0.5, 0.5],
		11 : [0.5, 0.5, 0.5, 0.5],
		12 : [0.5, 0.5, 0.5, 0.5],
		13 : [0.5, 0.5, 0.5, 0.5],
		14 : [0.5, 0.5, 0.5, 0.5],
		15 : [0.5, 0.5, 0.5, 0.5],
		16 : [0.5, 0.5, 0.5, 0.5],
		17 : [0.5, 0.5, 0.5, 0.5],
		18 : [0.5, 0.5, 0.5, 0.5],
		19 : [0.5, 0.5, 0.5, 0.5],
		20 : [0.5, 0.5, 0.5, 0.5],
		21 : [0.5, 0.5, 0.5, 0.5]
		}
	while trial < 2000:
		qdict, wins = game(qdict, trial, wins)
		reslist = []
		qlist = []
		for key in qdict.keys():
			qlist.append(qdict[key])
		reslist.append(qlist)
		perc = float(wins)/float(trial)
		reslist.append(perc)
		resfile = open('resultsDealer.csv', 'a')
		reswriter = csv.writer(resfile)
		reswriter.writerow(reslist)
		resfile.close()
		trial += 1
