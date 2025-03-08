import pygame
from constants import *
from squareshape import SquareShape

class Snake(SquareShape):
    def __init__(self, x, y):
        super().__init__(x, y, SNAKE_SIZE, SNAKE_SIZE)
        self.rotation = 0
        self.move_timer = 0.0
        self.turn_timer = 0
        self.length = SNAKE_LENGTH        

    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.position.x,self.position.y, self.width, self.height))

    def update(self, dt, player):
        if self.turn_timer > 0:
            self.turn_timer -= dt * SNAKE_SPEED * (1 + (self.length//10))
            if self.turn_timer <0:
                self.turn_timer = 0
        if self.move_timer > 0.0:
            self.move_timer -= dt * SNAKE_SPEED * (1 + (self.length//10))
            if self.move_timer < 0.0:
                self.move_timer = 0.0
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1)
        if keys[pygame.K_d]:
            self.rotate(1)
    
    def rotate(self, direction):
        if self.turn_timer > 0:
            return
        self.turn_timer = 1
        self.rotation += 90 * direction

    def move(self, dt):
        if self.move_timer > 0:
            return
        forward = pygame.Vector2(0, SNAKE_SIZE).rotate(self.rotation)
        self.position += forward
        self.move_timer = 1
        
