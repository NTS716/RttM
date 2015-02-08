import pygame
from colors import *
from prefs import screenRes 

class Rocket(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((screenRes[0] / 16, screenRes[0] / 16))
		self.image.fill(WHITE)

		self.rect = self.image.get_rect()

		self.rect.x = (screenRes[0] / 2 - (screenRes[0] / 16)) 
		self.rect.y = (screenRes[1] - (screenRes[1] / 6))
