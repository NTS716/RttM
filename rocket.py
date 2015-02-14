import pygame
from prefs import screenRes, useImages, rocketSpeed, collision
from colors import WHITE

class Rocket(pygame.sprite.Sprite):
	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		if useImages == False:
			self.size = ((screenRes[0] / 16), (screenRes[1] / 10))

			self.image = pygame.Surface(self.size)
			self.image.fill(WHITE)

		self.rect = self.image.get_rect()
		
		#set the default position
		self.rect.x = ((screenRes[0] / 2) - self.size[0])
		self.rect.y = (screenRes[1] - self.size[1])

		self.lives = 3

	#Checks if the user is pressing a key
	def pressing(self, key):
		if pygame.key.get_pressed()[key]:
			return True
		else:
			return False

	#moves the rocket
	def move(self):
		#UP
		if self.pressing(pygame.K_w) and self.rect.y > 0:
			self.rect.y -= rocketSpeed[1]
		#DOWN
		elif self.pressing(pygame.K_s) and self.rect.y < (screenRes[1] - self.size[1]):
			self.rect.y += rocketSpeed[1]
		#LEFT
		if self.pressing(pygame.K_a) and self.rect.x > 0:
			self.rect.x -= rocketSpeed[0]
		#RIGHT
		elif self.pressing(pygame.K_d) and self.rect.x < (screenRes[0] - self.size[0]):
			self.rect.x += rocketSpeed[0]
	
	#when the rocket gets hit
	def getHit(self):
		self.rect.x = ((screenRes[0] / 2) - self.size[0])
		self.rect.y = (screenRes[1] - self.size[1])
		self.lives -= 1
		collision = False
