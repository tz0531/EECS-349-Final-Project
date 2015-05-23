from deck import *
from Card import *
from bjutils import *
from player import *

##info to send to decider##
#ace or not
#dealer's face card
#cards played (len deck)
#value of hand(s)


class Dealer:
	def __init__(self):
		self.deck = Deck()
		self.hand = []
		self.hole = None

	def dealerDraw(self):
		self.hand.append(self.hole)
		while valHand(self.hand) < 17:
			self.hand.append(self.deck.cards.Pop(0))
	
	def deal(self,p):
		p.hand.append(self.deck.cards.pop(0))
		p.hand.append(self.deck.cards.pop(0))
		for card in p.hand:
			p.seen.append(card)
		self.hand.append(self.deck.cards.pop(0))
		p.seen.append(self.hand[0])
		self.hole = self.deck.cards.pop(0)

	def playRound(self, p):
		#dec = p.decide()
		dec = "HIT"
		if dec == "HIT":
			p.hand.append(self.deck.cards.pop(0))
			p.seen.append(p.hand[-1])
			#print(type(valHand(p.hand)))
			if valHand(p.hand) > 21:
				return -1
		elif dec == "STAND":
			self.dealerDraw()
			if valHand(self.hand) > 21:
				return 1
			elif valHand(p.hand) > 21:
				return -1
			if valHand(self.hand) > bjutils.valHand(p.hand):
				return -1
			elif valHand(self.hand) < bjutils.valHand(p.hand):
				return 1
			elif valHand(self.hand) == bjutils.valHand(p.hand):
				return 0
		return 2		
