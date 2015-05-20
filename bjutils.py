from Card import *

def valHand(hand):
	val = 0
	for card in hand:
		if "Ace" in card.name:
			if val <= 9:
				val += 11
			else:
				val += 1
		else:
			val += card.val
	return val
