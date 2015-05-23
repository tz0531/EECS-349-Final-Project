from deck import *
from bjutils import *
from dealer import *
from Card import *

class Player:
	def __init__(self):
		self.hand = []
		self.seen = []

        #def hit(dealer):
                #self.hand.append(dealer.deck.Pop(0))
	##Implemented this above function in dealer.py
        def canSplit(self):
                if len(self.hand) == 2 and self.hand[0].value == self.hand[1].value:
                        return True
                else:
                        return False
	
	def decide(self):
		#player decision code goes here
		return 0
