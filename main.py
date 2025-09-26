from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from Shot import *
import pygame

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, projectiles)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(
        f"Screen width: {SCREEN_WIDTH} \n"
        f"Screen height: {SCREEN_HEIGHT}"
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                pygame.quit()
                return
            for shot in projectiles:
                if shot.collision_check(asteroid):
                    asteroid.split()
                    shot.kill()
        screen.fill((0,0,0,))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
