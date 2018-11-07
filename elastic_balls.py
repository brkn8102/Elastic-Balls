import numpy as np
import random
import  numpy.linalg as la
import itertools

colors = [(232,232,232), (240,213,25), (210,59,25), (19,53,205), (0,0,0)]

class Ball:
	def __init__(self, m, r, c, x, y, vx, vy):
		self.m = m
		self.r = r
		self.c = c
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def pos(self):
		return np.array([self.x, self.y])

	def vel(self):
		return np.array([self.vx, self.vy])

	def velAngle(self):
		r = np.sqrt(self.vx**2 + self.vy**2)
		a = np.arccos(self.vx / r)
		if self.vy < 0:
			a = 2*np.pi - a
		return a

	def move(self):
		self.x += self.vx
		self.y += self.vy

	def kineticEnergy(self):
		return 1/2*self.m*(self.vx**2 + self.vy**2)

class BallSystem:
	def __init__(self, width, height, balls = []):
		self.balls = balls
		self.ballPairs = list(itertools.combinations(self.balls, 2))
		self.areColliding = [False for i in range(len(self.ballPairs))]
		self.width = width
		self.height = height
		self.step = 0

	def addBall(self, m, r, c, x, y, vx, vy):
		self.balls.append(Ball(m, r, c, x, y, vx, vy))
		self.ballPairs = list(itertools.combinations(self.balls, 2))
		self.areColliding = [False for i in range(len(self.ballPairs))]

	def addRandomBalls(self, n, maxSpeed=10, color=random.choice(colors), angle=2*np.pi*random.random()):
		for i in range(n):
			m = 0.1+random.random()
			r = int( np.rint(20*m) )
			c = color
			x = random.randint(r, self.width-r)
			y = random.randint(r, self.height-r)

			speed = maxSpeed*random.random()
			vx = speed*np.cos(angle)
			vy = speed*np.sin(angle)

			self.addBall(m, r, c, x, y, vx, vy)

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

		[b1.vx, b1.vy] = v + b2.vel()
		[b2.vx, b2.vy] = w + b2.vel()

	def nextStep(self):
		self.step += 1

		for b in self.balls:
			b.move()

		# wall collision
		for b in self.balls:
			# left or right wall
			if b.x - b.r < 0:
				b.vx = abs(b.vx)
			elif self.width < b.x + b.r:
				b.vx = -abs(b.vx)

			# top or bottom wall
			if b.y - b.r < 0:
				b.vy = abs(b.vy)
			elif self.height < b.y + b.r:
				b.vy = -abs(b.vy)

		# ball collision
		for i in range(len(self.ballPairs)):
			(b1, b2) = self.ballPairs[i]
			if la.norm(b2.pos() - b1.pos()) < b1.r + b2.r:
				if not self.areColliding[i]:
					self.areColliding[i] = True
					self.collideBalls(b1, b2)
			else:
				self.areColliding[i] = False

	def kineticEnergies(self):
		return np.array([b.kineticEnergy() for b in self.balls])
				
	def totalKineticEnergy(self):
		return np.sum(self.kineticEnergies())