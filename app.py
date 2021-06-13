import time
import random
import pygame 


pygame.init()

red = (230, 0, 0)
green = (115, 230, 0)
blue = (0, 172, 230)
yellow = (255, 255, 128)
white = (255, 255, 255)
black = (0, 0, 0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('蛇 - へび')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 20

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def get_score(score):
	value = score_font.render('Score: ' + str(score), True, yellow)
	dis.blit(value, [0, 0])


def snake(snake_block, snake_body):
	for i in snake_body:
		pygame.draw.rect(dis, green, [i[0], i[1], snake_block, snake_block])


def message(msg, color):
	message = font_style.render(msg, True, color)
	dis.blit(message, [dis_width/6, dis_height/3])


def game_loop():
	game_over = False
	game_close = False

	x = dis_width/2
	y = dis_height/2

	delta_x = 0
	delta_y = 0

	snake_body = []
	snake_len = 1

	food_x = round(random.randrange(0, dis_width - snake_block) / 10) * 10
	food_y = round(random.randrange(0, dis_height - snake_block) / 10) * 10

	while not game_over:

		while game_close == True:
			dis.fill(blue)
			message('You Lost! Press Q-Quit or Space-Play Again', red)
			get_score(snake_len -1)
			
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_SPACE:
						game_loop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					delta_x = snake_block
					delta_y = 0
				elif event.key == pygame.K_LEFT:
					delta_x = -snake_block
					delta_y = 0
				elif event.key == pygame.K_UP:
					delta_x = 0
					delta_y = -snake_block
				elif event.key == pygame.K_DOWN:
					delta_x = 0
					delta_y = snake_block

			if x >= dis_width or x < 0 \
			or y >= dis_height or y < 0:
				game_close = True

			x += delta_x
			y += delta_y

			dis.fill(blue)

			pygame.draw.rect(dis, red, [food_x, food_y, snake_block, snake_block])
			
			snake_head = []

			snake_head.append(x)
			snake_head.append(y)

			snake_body.append(snake_head)

			if len(snake_body) > snake_len:
				del snake_body[0]

			for i in snake_body[:-1]:
				if i == snake_head:
					game_over = True

			snake(snake_block, snake_body)
			get_score(snake_len -1)

			pygame.display.update()

			if x == food_x and y == food_y:
				food_x = round(random.randrange(0, dis_width - snake_block) / 10) * 10
				food_y = round(random.randrange(0, dis_height - snake_block) / 10) * 10
				snake_len += 1

			clock.tick(snake_speed)
	pygame.quit()
	quit()

game_loop()
