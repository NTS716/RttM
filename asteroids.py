import pygame
from prefs import screenRes, useImages, asteroidCount, asteroidSpeed
from random import randint
from colors import RED

class Asteroid(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.size = (100, 100)
		
		if useImages == False:
			self.image = pygame.Surface(self.size)
			self.image.fill(RED)
		
		self.rect = self.image.get_rect()

	def shuffle(self):
		xSize = randint((screenRes[0] / 14), (screenRes[0] / 7))
		ySize = randint((screenRes[1] / 10), (screenRes[1] / 5))
		self.size = (xSize, ySize)
		
		if useImages == False:
			self.image = pygame.Surface(self.size)
			self.image.fill(RED)

		self.rect.x = randint(0, screenRes[0] - self.size[0]) 
		self.rect.y = (randint(-screenRes[1], 0))

	def fall(self):
		if self.rect.y < screenRes[1]:
			self.rect.y += asteroidSpeed
		else:
			self.shuffle()
