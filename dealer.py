from deck import *
from Card import *
from bjutils import *
from player import *

class Dealer:
	def __init__():
		self.deck = Deck()
		self.hand = []
		self.hole = None

	def dealerDraw():
		self.hand.append(self.hole)
		while bjutils.valHand(self.hand) < 17:
			self.hand.append(self.deck.Pop(0))
	
	def deal(players):
		for p in players:
			p.hand.append(self.deck.Pop(0))
			p.hand.append(self.deck.Pop(0))
		self.hand.append(self.deck.Pop(0))
		self.hole = self.deck.Pop(0)

	def playRound(players):
		for p in players:
			pmove = p.decide()
			if pmove == 
