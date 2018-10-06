import sys, pygame as pg, ball
pg.init()

width, height = 1280, 750
black = 0, 0, 0
white = 255, 255, 255

b = ball.Ball(1, 10, width//2, height//2, 10, 10)

screen = pg.display.set_mode([width, height])
pg.display.set_caption("Elastic Balls")

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()

	b.move()

	# handle wall collision
	if b.x - b.r < 0 or width < b.x + b.r:
		b.vx = -b.vx
	if b.y - b.r < 0 or height < b.y + b.r:
		b.vy = -b.vy

	screen.fill(white)
	pg.draw.circle(screen, black, (b.x, b.y), 10)
	pg.display.flip()

	#pg.time.wait(100)