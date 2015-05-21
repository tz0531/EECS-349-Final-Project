#Builds deck based on rules found at http://www.bigmcasino.com/learn-more/what-are-the-card-values-in-black-jack/

#Ace is automatically assigned a value of 11 unless it causes a bust

from Card import *
import random

class Deck:
	suits = ["clubs", "spades", "hearts", "diamonds"]
	types = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
	def __init__(self):
		self.cards = []
		for s in self.suits:
			for t in self.types:
				cname = t+" of "+s
				if t == "Jack" or t == "Queen" or t == "King":
					cval = 10
				elif t == "Ace":
					cval = 11
				else:
					cval = int(t)
				nc = Card(cname, cval)
				self.cards.append(nc)
		self.cards = random.sample(self.cards, len(self.cards))

if __name__ == "__main__":
	d = Deck()
	for c in d.cards:
		print(c.name)
