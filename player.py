from deck import *
from bjutils import *
from dealer import *
from Card import *

class Player:
	def __init__():
		self.hand = []

        def hit(dealer):
                self.hand.append(dealer.deck.Pop(0))

        def canSplit():
                if len(self.hand) == 2 and self.hand[0].value == self.hand[1].value:
                        return True
                else:
                        return False
	
	def decide():
		#player decision code goes here
		return 0
