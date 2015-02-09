import pygame
from prefs import screenRes, asteroidSpeed
from random import randint
from colors import RED

class Asteroid(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.size = (50)
		self.image = pygame.Surface((self.size, self.size))
		self.image.fill(RED)

		self.rect = self.image.get_rect()

	def shuffle(self):

		self.size = randint(screenRes[0] / 16, screenRes[0] / 8)
		self.image = pygame.Surface((self.size, self.size))
		self.image.fill(RED)

		self.rect.x = randint(0, screenRes[0] - self.size) 
		self.rect.y = (randint(-screenRes[1], 0))

	def fall(self):
		if self.rect.y < screenRes[1]:
			self.rect.y += asteroidSpeed
		else:
			self.shuffle()
