from deck import *
from Card import *
from bjutils import *
from player import *
from dealer import *
import csv

global Q_old

def game():
	p = Player()
	d = Dealer()
	d.deal(p)
	status = 2
	while status == 2:
		status = d.playRound(p)
		hasAce = 0
		for card in p.hand:
			if "Ace" in card.name:
				hasAce = 1
		dfc = d.hand[0].value
		seen = []
		for card in p.seen:
			seen.append(card.value)
		phand = []
		for card in p.hand:
			phand.append(card.value)
		datafile = open('data.csv', 'a')
		datacsv = csv.writer(datafile)
		datacsv.writerow([hasAce, dfc, seen, phand, status])
		datafile.close()

if __name__ == "__main__":
	game()
