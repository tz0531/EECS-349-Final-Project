from deck import *
from Card import *
from bjutils import *
from player import *
from dealer import *
from qlearn import *
import csv
import time

global Q_old

def game(qdict, trial):
	q = Qlearn()
	p = Player()
	d = Dealer()
	d.deal(p)
	status = 2
	print("starting a game...")
	time.sleep(1)
	while status == 2:
		initval = valHand(p.hand)
		qlist = qdict[initval]
		Q1 = qlist[0]
		Q2 = qlist[1]
		pchoice = q.epsilonGreedy(Q1, Q2, 0.1)
		if pchoice == Q1:
			print("Player chose to HIT")
			time.sleep(1)
			status = d.playRound(p, "HIT")
		elif pchoice == Q2: 
			print("Player chose to STAND")
			time.sleep(1)
			status = d.playRound(p, "STAND")
		Q1, Q2 = q.evaluate(p, Q1, Q2, pchoice, status, trial)
		qlist = [Q1, Q2]
		qdict[initval] = qlist
		#hasAce = 0
		#for card in p.hand:
		#	if "Ace" in card.name:
		#		hasAce = 1
		#dfc = d.hand[0].value
		#seen = []
		#for card in p.seen:
		#	seen.append(card.value)
		#phand = []
		#for card in p.hand:
		#	phand.append(card.value)
		#datafile = open('data.csv', 'a')
		#datacsv = csv.writer(datafile)
		#datacsv.writerow([hasAce, dfc, seen, phand, status])
		#datafile.close()
	return qdict

if __name__ == "__main__":
	#Q1 = 0.5
	#Q2 = 0.5
	trial = 1
	qdict = {
		4 : [0.5, 0.5],
		5 : [0.5, 0.5],
		6 : [0.5, 0.5],
		7 : [0.5, 0.5],
		8 : [0.5, 0.5],
		9 : [0.5, 0.5],
		10 : [0.5, 0.5],
		11 : [0.5, 0.5],
		12 : [0.5, 0.5],
		13 : [0.5, 0.5],
		14 : [0.5, 0.5],
		15 : [0.5, 0.5],
		16 : [0.5, 0.5],
		17 : [0.5, 0.5],
		18 : [0.5, 0.5],
		19 : [0.5, 0.5],
		20 : [0.5, 0.5],
		21 : [0.5, 0.5]
		}
	while True:
		qdict = game(qdict, trial)
		for key in qdict.keys():
			print(qdict[key])
		time.sleep(5)
		trial += 1
