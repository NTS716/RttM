import pygame
from pygame.locals import *
import sys

#Debugging preferences
fps = 35

def main():
    #Initalize Pygame
    pygame.init()

    #create the display and caption
    SCREEN = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rocket to the Moon")

    #create the clock object and fps
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
