import pygame as pg
import sys
from food import *
from board import *
from settings import *
from snake import *

class Game(object):
	def __init__(self):
		check_errors = pg.init()

		if check_errors[1] > 0:
			print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
			sys.exit(-1)
		else:
			print('[+] Game successfully initialised')

		high_scores = open(r"high_scores", "r+")
		self.high_score = high_scores.readline()
		high_scores.close()
		self.clock = pg.time.Clock()
		self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
		self.surface = pg.Surface(self.screen.get_size())
		self.surface = self.surface.convert()
		self.board = Board(self.surface)
		self.snake = Snake()
		self.food = Food()
		self.my_font = pg.font.SysFont("monospace", 16)
		self.board.draw_grid(self.surface)

	def new(self):
		pg.display.set_caption("High Score: " + self.high_score)
		self.run()

	def run(self):
		while(True):
			self.clock.tick(FPS)
			self.events()
			self.draw()
			self.update()
			self.set_new_high_score()

	def events(self):
		self.snake.handle_key_strokes()
		self.board.draw_grid(self.surface)
		self.snake.move()

		if self.snake.get_head_position() == self.food.get_position():
			self.snake.length += 1
			self.snake.score += 1
			self.food.randomize_position()

	def update(self):
		pg.display.update()

	def draw(self):
		self.snake.draw(self.surface)
		self.food.draw(self.surface)
		self.screen.blit(self.surface, (0, 0))
		text = self.my_font.render("Score {0}".format(self.snake.score), 1, (255, 0, 0))
		self.screen.blit(text, (5, GRID_SIZE))

	def set_new_high_score(self):
		if self.snake.score > int(self.high_score):
			self.high_score = str(self.snake.score)
			pg.display.set_caption("High Score: " + self.high_score)
			high_scores = open(r"high_scores", "w")
			high_scores.write(self.high_score)
			high_scores.close()