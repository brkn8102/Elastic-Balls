import sys, pygame as pg, numpy as np, ball
from numpy import linalg as la
from itertools import combinations
pg.init()

width, height = 1280, 750
black = 0, 0, 0
white = 255, 255, 255

ball1 = ball.Ball(1, 50, width//2, height//2, 10, 10)
ball2 = ball.Ball(2, 100, 3*width//4, 3*height//4, -10, 10)
ball3 = ball.Ball(3, 150, width//4, height//4, -10, 10)

balls = [ball1, ball2, ball3]

screen = pg.display.set_mode([width, height])
pg.display.set_caption("Elastic Balls")

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

	for b in balls:
		b.move()

	# wall collision
	for b in balls:
		if b.x - b.r < 0 or width < b.x + b.r:
			b.vx = -b.vx
		if b.y - b.r < 0 or height < b.y + b.r:
			b.vy = -b.vy

	# ball collision
	for (b1, b2) in list(combinations(balls, 2)):
		if la.norm(b2.pos() - b1.pos()) < b1.r + b2.r:
			ball.collide(b1,b2)

	screen.fill(white)
	for b in balls:
		pg.draw.circle(screen, black, (b.x, b.y), b.r)
	pg.display.flip()

	#pg.time.wait(100)