import pygame
from constants import *
from squareshape import SquareShape

class Tail(SquareShape):
    def __init__(self, x, y, count):
        super().__init__(x, y, SNAKE_SIZE, SNAKE_SIZE)
        self.count = count

    def draw(self, screen):
        pygame.draw.rect(screen, "white",(self.position.x,self.position.y, self.width, self.height))

    def update(self, dt, player):
        pass