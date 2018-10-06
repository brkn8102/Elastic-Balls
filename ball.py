import numpy as np
from numpy import linalg as LA

class Ball:
	def __init__(self, m, r, x, y, vx, vy):
		self.m = m
		self.r = r
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def move(self):
		self.x += self.vx
		self.y += self.vy