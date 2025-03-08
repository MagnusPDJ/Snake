import pygame
from constants import *
from squareshape import SquareShape

class Food(SquareShape):
    def __init__(self, x, y):
        super().__init__(x, y, FOOD_SIZE, FOOD_SIZE)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "red",(self.position.x,self.position.y, self.width, self.height))

    def update(self, dt):
        pass