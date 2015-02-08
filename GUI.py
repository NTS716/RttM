import pygame
from pygame.locals import *
import sys
from space import Space
from prefs import screenRes, fps

def main():
    #Initalize Pygame
    pygame.init()

    #create the display and caption
    SCREEN = pygame.display.set_mode((screenRes))
    pygame.display.set_caption("Rocket to the Moon")

    #create the clock object
    clock = pygame.time.Clock()

    #create the space background
    space = Space()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        space.draw(SCREEN)
        space.scroll()
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
