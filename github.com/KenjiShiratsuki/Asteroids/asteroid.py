import pygame # type: ignore
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        newvector1 = self.velocity.rotate(random_angle) * 1.2
        newvector2 = self.velocity.rotate(-random_angle) * 1.2
        newradius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(*self.position, newradius)
        new_asteroid_2 = Asteroid(*self.position, newradius)

        new_asteroid_1.velocity = newvector1
        new_asteroid_2.velocity = newvector2