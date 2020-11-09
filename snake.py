import pygame as pg
import sys
from settings import *

class Snake(object):
	def __init__(self):
		self.length = 3
		self.positions = [
						  ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), 
						   (SCREEN_WIDTH / 2) - GRID_SIZE, (SCREEN_HEIGHT / 2), 
						   (SCREEN_WIDTH / 2) - 2 * GRID_SIZE, (SCREEN_HEIGHT / 2))
						  ]
		self.direction = 'r'
		self.color = pg.Color(0, 255, 0)
		self.score = 0

	def get_head_position(self):
		return self.positions[0]

	def change_direction(self, new_direction):
		if new_direction == 'r' and self.direction != 'l':
			self.direction = 'r'
		if new_direction == 'l' and self.direction != 'r':
			self.direction = 'l'
		if new_direction == 'u' and self.direction != 'd':
			self.direction = 'u'
		if new_direction == 'd' and self.direction != 'u':
			self.direction = 'd'

	def move(self):
		head_position = self.get_head_position()

		if self.direction == 'u':
			new_position = (((head_position[0] + (0 * GRID_SIZE))), 
							(head_position[1] + (-1 * GRID_SIZE)))
		if self.direction == 'd':
			new_position = (((head_position[0] + (0 * GRID_SIZE))), 
							(head_position[1] + (1 * GRID_SIZE)))
		if self.direction == 'l':
			new_position = (((head_position[0] + (-1 * GRID_SIZE))), 
							(head_position[1] + (0 * GRID_SIZE)))
		if self.direction == 'r':
			new_position = (((head_position[0] + (1 * GRID_SIZE))), 
							(head_position[1] + (0 * GRID_SIZE)))

		if new_position in self.positions[2:]:
			self.reset()
		elif new_position[0] < 0 or new_position[0] > SCREEN_HEIGHT - 10:
			self.reset()
		elif new_position[1] < 0 or new_position[1] > SCREEN_WIDTH - 10:
			self.reset()
		else:
			self.positions.insert(0, new_position)
			if len(self.positions) > self.length:
				self.positions.pop()

	def reset(self):
		self.length = 3
		self.positions = [
						  ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), 
						   (SCREEN_WIDTH / 2) - GRID_SIZE, (SCREEN_HEIGHT / 2), 
						   (SCREEN_WIDTH / 2) - 2 * GRID_SIZE, (SCREEN_HEIGHT / 2))
						  ]
		self.direction = 'r'
		self.color = pg.Color(0, 255, 0)
		self.score = 0

	def draw(self, surface):
		for position in self.positions:
			rectangle = pg.Rect((int(position[0]), int(position[1])), (int(GRID_SIZE), int(GRID_SIZE)))
			pg.draw.rect(surface, self.color, rectangle)
			pg.draw.rect(surface, pg.Color(0, 255, 0), rectangle, 1)

	def handle_key_strokes(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_UP:
					self.change_direction('u')
				if event.key == pg.K_DOWN:
					self.change_direction('d')
				if event.key == pg.K_LEFT:
					self.change_direction('l')
				if event.key == pg.K_RIGHT:
					self.change_direction('r')