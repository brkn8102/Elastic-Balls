import sys, pygame as pg, numpy as np, random
import matplotlib.pyplot as plt, elastic_balls

pg.init()

width, height = 1280, 750

screen = pg.display.set_mode([width, height])
pg.display.set_caption("Elastic Balls")

black = (0, 0, 0)
white = (255, 255, 255)

NUM_BALLS = 200
bs = elastic_balls.BallSystem(width, height)
bs.addRandomBalls(NUM_BALLS)
for b in bs.balls:
	b.m = 2
	b.r = 10
	b.c = white

	speed = 20
	theta = 2*np.pi*random.random()
	b.vx = speed*np.cos(theta)
	b.vy = speed*np.sin(theta)
for i in range(NUM_BALLS//2):
	bs.balls[i].vx *= 1.4
	bs.balls[i].vy *= 1.4

MAX_STEPS = 10
k = np.zeros((MAX_STEPS, NUM_BALLS))

while bs.step < MAX_STEPS:
	print(bs.step)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

	for i in range(NUM_BALLS):
		k[bs.step][i] = bs.balls[i].kineticEnergy()

	screen.fill(black)
	for b in bs.balls:
		[bx, by] = np.rint(b.pos()).astype(int) 
		pg.draw.circle(screen, b.c, (bx, by), b.r)
	pg.display.flip()

	bs.nextStep()

s = np.repeat(np.arange(MAX_STEPS), NUM_BALLS)
plt.hist2d(k.flatten(), s, bins=(50,MAX_STEPS))
plt.xlabel('Kinetic Energy')
plt.ylabel('Step')
plt.show()