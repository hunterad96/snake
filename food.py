import pygame as pg
import random
from settings import *

class Food(object):
	def __init__(self):
		self.position = (0, 0)
		self.color = pg.Color(255, 0 ,0)
		self.randomize_position()

	def get_position(self):
		return self.position

	def randomize_position(self):
		self.position = (random.randint(0, GRID_WIDTH-1)*GRID_SIZE, random.randint(0, GRID_HEIGHT-1)*GRID_SIZE)

	def draw(self, surface):
		rectangle = pg.Rect((self.position[0], self.position[1]), (int(GRID_SIZE), int(GRID_SIZE)))
		pg.draw.rect(surface, self.color, rectangle)
		pg.draw.rect(surface, pg.Color(255, 0, 0), rectangle, 1)