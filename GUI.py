import pygame
from pygame.locals import *
import sys
from space import Space
from rocket import Rocket
from prefs import screenRes, fps, asteroidCount, collision
from asteroids import Asteroid

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

    #create the sprite list
    allSprites = pygame.sprite.Group()
    asteroidSprites = pygame.sprite.Group()

    #create the rocket
    rocket = Rocket()
    allSprites.add(rocket)

    #create the asteroids
    for i in range(asteroidCount):
        asteroid = Asteroid()
        asteroid.shuffle()
        asteroidSprites.add(asteroid)
        allSprites.add(asteroid)

    #create collisions
    def checkCollides():
        collides = pygame.sprite.spritecollide(rocket, asteroidSprites, True)

    #update function
    def update():
        space.draw(SCREEN)
        allSprites.draw(SCREEN)

        space.scroll()
        rocket.move()
        for asteroid in asteroidSprites:
            asteroid.fall()
        if collision == True:
            checkCollides() 

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                print pygame.mouse.get_pos()
        update()
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
