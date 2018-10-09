import sys, pygame as pg, numpy as np, elastic_balls
from numpy import linalg as la

pg.init()

width, height = 1280, 750
black = (0, 0, 0)
white = (255, 255, 255)

bs = elastic_balls.BallSystem(width, height)
bs.addRandomBalls(20)
for b in bs.balls:
	b.c = white
bs.addBall(10**10, 150, white, width//2, height//2, 10, 0)

screen = pg.display.set_mode()
pg.display.set_caption("Elastic Balls")

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

	bs.nextStep()

	screen.fill(black)
	for b in bs.balls:
		[bx, by] = np.rint(b.pos()).astype(int) 
		pg.draw.circle(screen, b.c, (bx, by), b.r)
	pg.display.flip()

	#pg.time.wait(10)