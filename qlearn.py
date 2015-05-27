from bjutils import *
import random
import time

class Qlearn:
	def epsilonGreedy(self, Q1, Q2, epsilon):
		decint = random.randint(1, 100)
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

	def evaluate(self, p, Q1, Q2, choice, status, trial):
		alpha = 1/(trial**0.5)
		gamma = 0.9
		maxa = 1
		if choice == Q1:
			Q1 = Q1 + alpha*(self.reward(p, status) + gamma*maxa - Q1)
			print("Q1 is now: "+str(Q1))
			print("Q2 remains: "+str(Q2))
			time.sleep(1)	
			return Q1, Q2
		elif choice == Q2:
			Q2 = Q2 + alpha*(self.reward(p, status) + gamma*maxa - Q2)
			print("Q1 remains: "+str(Q1))
			print("Q2 is now: "+str(Q2))
			time.sleep(1)
			return Q1, Q2
		else:
			print("problem")

	def reward(self, p, status):
		if valHand(p.hand) > 21 or status == -1 or status == 0:
			return 0.0
		else:
			return 1/(22-valHand(p.hand))
