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

	def evaluate(self, p, Q1, Q2, Q3, Q4, choice, status, trial, wins):
		alpha = 1/(trial**0.1)
		#alpha = 1/(trial*0.15)
		#alpha = 0.1
		gamma = 0.99
		#gamma = 0.05
		maxa = 1
		if status == 1:
			wins += 1
		if choice == Q1:
			Q1 = Q1 + alpha*(self.rewardHit(p, status) + gamma*maxa - Q1)
			#print("Q1 is now: "+str(Q1))
			#print("Q2 remains: "+str(Q2))
			#time.sleep(1)	
			return Q1, Q2, Q3, Q4, wins
		elif choice == Q2:
			Q2 = Q2 + alpha*(self.rewardStay(p, status) + gamma*maxa - Q2)
			#print("Q1 remains: "+str(Q1))
			#print("Q2 is now: "+str(Q2))
			#time.sleep(1)
			return Q1, Q2, Q3, Q4, wins
		elif choice == Q3:
			Q3 = Q3 + alpha*(self.rewardHit(p, status) + gamma*maxa - Q3)
			return Q1, Q2, Q3, Q4, wins
		elif choice == Q4:
			Q4 = Q4 + alpha*(self.rewardStay(p, status) + gamma*maxa - Q4)
			return Q1, Q2, Q3, Q4, wins
		else:
			print("problem")
	def rewardHit(self, p, status):
		if status == -1:
			return -1
		else:
			rwd = valHand(p.hand) + random.randint(1, 11)
			if rwd >= 22:
				#return -1
				return 0
			else:
				return 1/(22-rwd)
	
	def rewardStay(self, p, status):
		if status == -1:
			return -1
		else:
			#return 0
			return 1/(22-valHand(p.hand))

	#def reward(self, p, status):
	#	if valHand(p.hand) > 21 or status == -1 or status == 0:
	#		return 0.0
	#	else:
	#		return 1/(22-valHand(p.hand))
