import numpy as np, random
from numpy import linalg as la
from itertools import combinations

class Ball:
	def __init__(self, m, r, x, y, vx, vy):
		self.m = m
		self.r = r
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def pos(self):
		return np.array([self.x, self.y])

	def vel(self):
		return np.array([self.vx, self.vy])

	def move(self):
		self.x += self.vx
		self.y += self.vy

class BallSystem:
	def __init__(self, width, height, balls = []):
		self.balls = balls
		self.ballPairs = list(combinations(self.balls, 2))
		self.areColliding = [ False for i in range(len(self.ballPairs)) ]
		self.width = width
		self.height = height

	def addBall(self, b):
		self.balls.append(b)
		self.ballPairs = list(combinations(self.balls, 2))
		self.areColliding = [ False for i in range(len(self.ballPairs)) ]

	def addRandomBalls(self, n):
		for i in range(n):
			m = random.random()
			r = random.randint(10,100)
			x = random.randint(0, self.width)
			y = random.randint(0, self.height)
			vx = random.randint(-10, 10)
			vy = random.randint(-10,10)
			self.addBall( Ball(m, r, x, y, vx, vy) )

	def moveAll(self):
		for b in self.balls:
			b.move()

	def collideBalls(self, b1, b2):
		n = b2.pos() - b1.pos()
		n = n/la.norm(n)

		m = np.array([n[1], -n[0]])

		mu = b2.m/b1.m

		u = b1.vel()-b2.vel()
		uPar = np.dot(u,n)
		uPer = np.dot(u,m)

		v = uPer*m + (1-mu)/(1+mu)*uPar*n

		w = 2/(1+mu)*uPar*n

		[b1.vx, b1.vy] = np.rint(v + b2.vel()).astype(int)
		[b2.vx, b2.vy] = np.rint(w + b2.vel()).astype(int)

	def step(self):
		for b in self.balls:
			b.move()

		# wall collision
		for b in self.balls:
			if b.x - b.r < 0 or self.width < b.x + b.r:
				b.vx = -b.vx
			if b.y - b.r < 0 or self.height < b.y + b.r:
				b.vy = -b.vy

		# ball collision
		for i in range(len(self.ballPairs)):
			(b1, b2) = self.ballPairs[i]
			if la.norm(b2.pos() - b1.pos()) < b1.r + b2.r:
				if not self.areColliding[i]:
					self.areColliding[i] = True
					self.collideBalls(b1, b2)
			else:
				self.areColliding[i] = False