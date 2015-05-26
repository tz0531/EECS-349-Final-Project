from bjutils import *
import random

class Qlearn:
	def epsilonGreedy(self, Q1, Q2, epsilon):
		decint = random.randint(1, 100):
		if decint > epsilon*100:
			if Q1 > Q2:
				return Q1
			else:
				return Q2
		else:
			randdec = random.randint(1, 2)
			if randdec == 1:
				return Q1
			else:
				return Q2

	def evaluate(self, p, Q1, Q2, choice):
		alpha = 0.9
		gamma = 0.9
		maxa = 1
		if choice == Q1:
			Q1 = Q1 + alpha*(reward(p) + gamma*maxa - Q1)
		elif choice == Q2:
			Q2 = Q2 + alpha*(reward(p) + gamma*maxa - Q2)
		else:
			print("problem")

	def reward(self, p):
		if valHand(p.hand) > 21:
			return 0.0
		else:
			return 1/(22-valHand(p.hand))
