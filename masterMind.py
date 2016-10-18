#Amalia Gómez Marcheco
#abeagomez@gmail.com 
#2016

import random

class masterMind:
	def __init__(self, goal):
		self.goal = goal

	def checkGuess(self, guess):
		r = [0,0]
		for i in range(0,len(self.goal)):
			if self.goal[i] == guess[i]:
				r[0] += 1
			elif self.goal[i] in guess:
				r[1] += 1
		print str(guess) + "  V: " + str(r[1]) + "   T: " + str(r[0])

	def isGoal(self, guess):
		for i in range(0,len(self.goal)):
			if self.goal[i] != guess[i]:
				return False
		return True

l = 0
goal = []
while l < 4:
	n = random.randint(1,9)
	if not n in goal:
		goal.append(n)
		l += 1
mm = masterMind(goal)
n = 0
while n<9:
	print "Guess"
	guess = raw_input()
	lguess = [int(i) for i in guess.split()]
	mm.checkGuess(lguess)
	if mm.isGoal(lguess):
		print "YES!"
		break
	n += 1
if n is 9:
	print "Ups"
