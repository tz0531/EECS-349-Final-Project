from Card import *

def valHand(hand):
	val = 0
	for card in hand:
		if "Ace" in card.name:
			if val <= 10:
				val += 11
			else:
				val += 1
				card.value = 1
		else:
			val += card.value
	return val
