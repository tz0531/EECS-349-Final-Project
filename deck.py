#Builds deck based on rules found at http://www.bigmcasino.com/learn-more/what-are-the-card-values-in-black-jack/

#Gave Ace cards none values to signal to the player that it needs to choose a value

from Card import *

class Deck:
	suits = ["clubs", "spades", "hearts", "diamonds"]
	types = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
	def __init__(self):
		self.cards = []
		for s in self.suits:
			for t in self.types:
				cname = t+" of "+s
				if t == "10" or t == "Jack" or t == "Queen" or t == "King":
					cval = 10
				elif t == "Ace":
					cval = None
				else:
					cval = int(t)
				nc = Card(cname, cval)
				self.cards.append(nc)

if __name__ == "__main__":
	d = Deck()
	print(len(d.cards))
