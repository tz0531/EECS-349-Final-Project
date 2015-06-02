from Card import *

def valHand(hand):
	val = 0
	aces = []
	for card in hand:
		if "Ace" in card.name:
			#if val <= 10:
			#	val += 11
			#else:
			#	val += 1
			#	card.value = 1
			aces.append(card)
		else:
			val += card.value
	for card in aces:
		if val <= 10:
			val += 11
		else:
			val += 1
	return val
