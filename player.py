import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # Draw to screen, in white, using triangle draw, with line width 2
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:            # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:            # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:            # Move forward
            self.move(dt)
        if keys[pygame.K_s]:            # Move backward
            self.move(-dt)
    
    def move(self, dt):                                         # 1. We start with a unit vector pointing straight up from (0, 0) to (0, 1).
        forward = pygame.Vector2(0, 1).rotate(self.rotation)    # 2. We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
        self.position += forward * PLAYER_SPEED * dt            # 3. We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
                                                                # 4. Add the vector to our position to move the player.