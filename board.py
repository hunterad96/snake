import pygame as pg
from settings import *

class Board(object):
	def __init__(self, surface):
		self.draw_grid(surface)

	def draw_grid(self, surface):
		for y in range(0, int(GRID_HEIGHT)):
			for x in range(0, int(GRID_WIDTH)):
				rectangle = pg.Rect((x * GRID_SIZE, y * GRID_SIZE), (int(GRID_SIZE), int(GRID_SIZE)))
				pg.draw.rect(surface, pg.Color(0, 0, 0), rectangle)