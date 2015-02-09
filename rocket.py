import pygame
from colors import *
from prefs import screenRes, rocketSpeed 

class Rocket(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.size = (screenRes[0] / 16, screenRes[0] / 14)
		self.image = pygame.Surface(self.size)
		self.image.fill(WHITE)

		self.rect = self.image.get_rect()

		#set the default position of the rocket
		self.rect.x = (screenRes[0] / 2 - (self.size[0])) 
		self.rect.y = (screenRes[1] - (screenRes[1] / 6))
	#Checks if a key is being pressed
	def pressing(self, key):
		if pygame.key.get_pressed()[key]:
			return True
		else:
			return False
	#Moves the rocket
	def move(self):
		if self.pressing(pygame.K_w) and self.rect.y > 0:
			self.rect.y -= rocketSpeed

		elif self.pressing(pygame.K_s) and self.rect.y < screenRes[1] - self.size[1]:
			self.rect.y += rocketSpeed

		if self.pressing(pygame.K_a) and self.rect.x > 0:
			self.rect.x -= rocketSpeed
	
		elif self.pressing(pygame.K_d) and self.rect.x < screenRes[0] - self.size[0]:
			self.rect.x += rocketSpeed
