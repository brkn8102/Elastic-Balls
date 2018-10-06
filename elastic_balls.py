import sys, pygame as pg, numpy as np, ball
from numpy import linalg as la

pg.init()

width, height = 1280, 750
black = 0, 0, 0
white = 255, 255, 255

bs = ball.BallSystem(width, height)
bs.addRandomBalls(10)

screen = pg.display.set_mode([width, height])
pg.display.set_caption("Elastic Balls")

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

	bs.step()

	screen.fill(white)
	for b in bs.balls:
		[bx, by] = np.rint(b.pos()).astype(int) 
		pg.draw.circle(screen, black, (bx, by), b.r)
	pg.display.flip()

	#pg.time.wait(10)