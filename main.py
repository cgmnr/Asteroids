import pygame
import sys
import random
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
    
        for sprite in  updatable:
            sprite.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game Over!")

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000
        




if __name__ == "__main__":
    main()
