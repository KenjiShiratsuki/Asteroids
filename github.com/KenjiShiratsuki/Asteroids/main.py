import pygame # type: ignore
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
def main():
    running = True
    paused = False
    pygame.init()
    font = pygame.font.Font(None, 74)
    pause_text = font.render("PAUSED", True, ("white"))
    text_rect = pause_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(SCREEN_WIDTH)
    print(SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    field = AsteroidField()
    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Exited game")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # 'P' key toggles pause
                    paused = not paused
        if not paused:
            updatable.update(dt)
            for obj in asteroids:
                if obj.collisioncheck(player) == True:
                    running = False
                    print("Game over!")
            for obj in asteroids:
                for shot in shots:
                    if obj.collisioncheck(shot) == True:
                        obj.kill()
                        shot.kill()
        screen.fill("black")
        for obj in drawable:   
            obj.draw(screen)
        if paused:
            screen.blit(pause_text, text_rect)
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()