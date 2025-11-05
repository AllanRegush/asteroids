from astroid import Asteroid
from astroidfield import AsteroidField
import pygame
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while(True):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
      updatable.update(dt)
      for asteroid in asteroids:
        if asteroid.check_collision(player):
          print("Game over!")
          return
        for shot in shots:
          if asteroid.check_collision(shot):
            asteroid.split()
            shot.kill()
      # asteroids.check_collision(player)
      pygame.Surface.fill(screen, 'black')
      for item in drawable:
        item.draw(screen)
      pygame.display.flip()
      dt = clk.tick(60) / 1000


if __name__ == "__main__":
    main()
