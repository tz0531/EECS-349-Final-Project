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
		if val + 11 > 21:
			val += 1
			card.value = 1
		else:
			val += 11
	return val

def flippedAce(hand):
	for card in hand:
		if card.value == 1:
			print("Has a flipped ace!")
			return True
	return False
