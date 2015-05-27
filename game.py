from deck import *
from Card import *
from bjutils import *
from player import *
from dealer import *
from qlearn import *
import csv
import time

global Q_old

def game(Q1, Q2, trial):
	q = Qlearn()
	p = Player()
	d = Dealer()
	d.deal(p)
	status = 2
	print("starting a game...")
	time.sleep(1)
	while status == 2:
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
	return Q1, Q2

if __name__ == "__main__":
	Q1 = 0.5
	Q2 = 0.5
	trial = 0
	while True:
		Q1, Q2 = game(Q1, Q2, trial)
		trial += 1
