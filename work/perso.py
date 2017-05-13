# -*- encoding:utf-8 -*-

from pygame import *
from config import *

class Perso:
	def __init__(self, right, left, up, down, map):
		self.right = image.load(right).convert_alpha()
		self.left = image.load(left).convert_alpha()
		self.up = image.load(up).convert_alpha()
		self.down = image.load(down).convert_alpha()

		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0

		self.direction = self.down
		self.map = map

	def move(self, direction):
		if direction == "right":
			if self.case_x < (nb_sprites - 1) and self.map.structure[self.case_y][self.case_x + 1] != 'W':
				self.case_x += 1
				self.x = self.case_x * sprite_size
			self.direction = self.right
		if direction == "left":
			if self.case_x > 0 and self.map.structure[self.case_y][self.case_x - 1] != 'W':
				self.case_x -= 1
				self.x = self.case_x * sprite_size
			self.direction = self.left
		if direction == "down":
			if self.case_y < (nb_sprites - 1) and self.map.structure[self.case_y + 1][self.case_x] != 'W':
				self.case_y += 1
				self.y = self.case_y * sprite_size
			self.direction = self.down
		if direction == "up":
			if self.case_y > 0 and self.map.structure[self.case_y - 1][self.case_x] != 'W':
				self.case_y -= 1
				self.y = self.case_y * sprite_size
			self.direction = self.up
