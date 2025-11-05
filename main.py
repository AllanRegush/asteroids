from astroid import Asteroid
from astroidfield import AsteroidField
import pygame
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from shot import Shot
from enum import Enum

class State(Enum):
  GAME = 1
  GAMEOVER = 2

score = 0

def main():
    global score
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    state = State.GAME
    clk = pygame.time.Clock()
    dt = 0
    font = pygame.font.SysFont("Arial", 32)
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
          state = State.GAMEOVER
          break
        for shot in shots:
          if asteroid.check_collision(shot):
            asteroid.split()
            shot.kill()
            score += 10
      # asteroids.check_collision(player)
      pygame.Surface.fill(screen, 'black')
      for item in drawable:
        item.draw(screen)
      if state == State.GAME:
        text_surface = font.render(f"Score: {score}", True, 'white')
        text_rect = text_surface.get_rect()
        text_rect.center = (90, 35)
        screen.blit(text_surface, text_rect)
      
      if state == State.GAMEOVER:
        text_surface = font.render(f"GAME OVER", True, 'white')
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
        screen.blit(text_surface, text_rect)
        
        text_surface = font.render(f"Your Score: {score}", True, 'white')
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text_surface, text_rect)
        
        text_surface = font.render(f"Press Space To Play again", True, 'white')
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
        screen.blit(text_surface, text_rect)
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
          score = 0
          state = State.GAME
      
      pygame.display.flip()
      dt = clk.tick(60) / 1000


if __name__ == "__main__":
    main()
