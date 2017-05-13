#!/usr/bin/python3
# -*- encoding:utf-8 -*-

from pygame import * # import de pygame
from config import * # import des variables
from map    import * # import de la map
from perso  import * # import du perso

#   //////////////////////////
#  ///// Initialisation /////
# //////////////////////////

init() # initialisation de pygame

window = display.set_mode((window_size, window_size))
icone = image.load(image_icone)
intro = image.load(image_intro).convert()

display.set_icon(icone)
display.set_caption(title)

#   /////////////////////////
#  ///// Boucle de jeu /////
# /////////////////////////

loop = True
while loop:
	window.blit(intro, (0, 0))
	display.flip()

	loop_intro = True
	loop_game = True
	while loop_intro:
		for evt in event.get():
			if evt.type == QUIT or evt.type == KEYDOWN and evt.key == K_ESCAPE:
				loop_intro = False
				loop_game = False
				loop = False
				load_map = 0
			elif evt.type == KEYDOWN and evt.key == K_RETURN:
				loop_intro = False
				load_map = "LinkToThePast"
	if load_map != 0:
		back = image.load(image_back).convert()
		map = Map(load_map)
		map.create()
		map.show(window)
		link = Perso("images/link_right.gif",
					"images/link_left.gif",
					"images/link_up.gif",
					"images/link_down.gif", map)

		while loop_game:
			for evt in event.get():
				if evt.type == QUIT:
					loop_game = False
					loop = False
				elif evt.type == KEYDOWN:
					if evt.key == K_ESCAPE:
						loop_game = False
					elif evt.key == K_RIGHT:
						link.move('right')
					elif evt.key == K_LEFT:
						link.move('left')
					elif evt.key == K_UP:
						link.move('up')
					elif evt.key == K_DOWN:
						link.move('down')
			window.blit(back, (0, 0))
			map.show(window)
			window.blit(link.direction, (link.x, link.y))
			display.flip()

			if map.structure[link.case_y][link.case_x] == 'T':
				loop_game = False
