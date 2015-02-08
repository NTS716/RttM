import pygame
from prefs import scrollSpeed, screenRes
import log

log.log(__file__)

class Space():
	def __init__(self):
		self.image = pygame.image.load("./assets/space.gif")
		self.scaledImage = pygame.transform.scale(self.image, screenRes)
		self.pos = (0,0)

	def draw(self, surface):
		surface.blit(self.scaledImage, self.pos)
		surface.blit(self.scaledImage, (self.pos[0], self.pos[1] + screenRes[1]))

	def scroll(self):
		self.pos = (self.pos[0], self.pos[1] - scrollSpeed)
		if self.pos[1] <= -screenRes[1]:
			self.pos = (0,0)
