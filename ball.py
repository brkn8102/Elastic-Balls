import numpy as np
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
	def __init__(self, width, height, balls):
		self.balls = balls
		self.width = width
		self.height = height

	def moveAll(self):
		for b in self.balls:
			b.move()

	def collide(self, b1, b2):
		n = b2.pos() - b1.pos()
		n = n/la.norm(n)

		m = np.array([n[1], -n[0]])

		mu = b2.m/b1.m

		u = b1.vel()-b2.vel()
		uPer = np.dot(u,n)
		uPar = np.dot(u,m)

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
		for (b1, b2) in list(combinations(self.balls, 2)):
			if la.norm(b2.pos() - b1.pos()) < b1.r + b2.r:
				self.collide(b1,b2)