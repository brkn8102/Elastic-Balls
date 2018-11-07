import sys
import random

import pygame as pg
import numpy as np
import matplotlib.pyplot as plt

import elastic_balls

animate = False

#screen size is 1280, 750
width, height = 1280, 750

if animate:
	pg.init()

	screen = pg.display.set_mode([width, height])
	pg.display.set_caption("Elastic Balls")

black = (0, 0, 0)
white = (255, 255, 255)

NUM_BALLS = 100
bs = elastic_balls.BallSystem(width, height)
bs.addRandomBalls(NUM_BALLS, color=white, maxSpeed=40, angle=0)

MAX_STEPS = 200
k = np.zeros((MAX_STEPS, NUM_BALLS))
a = np.zeros((MAX_STEPS, NUM_BALLS))

while bs.step < MAX_STEPS:
	print(bs.step)

	for i in range(NUM_BALLS):
		k[bs.step][i] = bs.balls[i].kineticEnergy()
		a[bs.step][i] = bs.balls[i].velAngle()

	if animate:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()

		screen.fill(black)
		for b in bs.balls:
			[bx, by] = np.rint(b.pos()).astype(int) 
			pg.draw.circle(screen, b.c, (bx, by), b.r)
		pg.display.flip()

	bs.nextStep()

#np.savetxt('data', k)

s = np.repeat(np.arange(MAX_STEPS), NUM_BALLS)

plt.hist2d(k.flatten(), s, bins=(50, MAX_STEPS))
plt.xlabel('Kinetic Energy')
plt.ylabel('Step')
plt.show()

plt.hist2d(a.flatten(), s, bins=(10, MAX_STEPS))
plt.xlabel('Angle')
plt.ylabel('Step')
plt.show()

densities, bin_edges = np.histogram(a[0], range=(0, 2*np.pi), bins=10, density=True)
ax = plt.subplot(111, projection='polar')
ax.bar(bin_edges[:-1], densities)
plt.show()

densities, bin_edges = np.histogram(a[-1], range=(0, 2*np.pi), bins=10, density=True)
ax = plt.subplot(111, projection='polar')
ax.bar(bin_edges[:-1], densities)
plt.show()