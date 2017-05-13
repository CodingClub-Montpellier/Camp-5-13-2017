# -*- encoding:utf-8 -*-

from pygame import *
from config import * # import des variables

class Map:
	def __init__(self, file):
		self.file = file
		self.structure = 0

	def show(self, window):
		wall = image.load(image_wall).convert_alpha()
		start = image.load(image_start).convert_alpha()
		triforce = image.load(image_triforce).convert_alpha()

		nb_line = 0
		for line in self.structure:
			nb_pos = 0
			for sprite in line:
				x = nb_pos * sprite_size
				y = nb_line * sprite_size
				if sprite == 'W':
					window.blit(wall, (x, y))
				elif sprite == 'L':
					window.blit(start, (x, y))
				elif sprite == 'T':
					window.blit(triforce, (x, y))
				nb_pos += 1
			nb_line += 1

	def create(self):
		with open(self.file, "r") as file:
			structure_map = []
			for line in file:
				map_line = []
				for sprite in line:
					map_line.append(sprite)
				structure_map.append(map_line)
			self.structure = structure_map
