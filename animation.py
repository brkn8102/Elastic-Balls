import sys, pygame as pg, numpy as np
import matplotlib.pyplot as plt, elastic_balls

pg.init()

width, height = 1280, 750

screen = pg.display.set_mode([width, height])
pg.display.set_caption("Elastic Balls")

black = (0, 0, 0)
white = (255, 255, 255)

NUM_BALLS = 100
bs = elastic_balls.BallSystem(width, height)
bs.addRandomBalls(NUM_BALLS)
for b in bs.balls:
	b.c = white

MAX_STEPS = 10
k = np.zeros((MAX_STEPS, NUM_BALLS))

while bs.step < MAX_STEPS:
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
	print(bs.step)

s = np.repeat(np.arange(MAX_STEPS), NUM_BALLS)
plt.hist2d(k.flatten(), s, bins=(10,MAX_STEPS))
plt.xlabel('Kinetic Energy')
plt.ylabel('Step')
plt.show()