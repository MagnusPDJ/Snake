import pygame
import random
from food import Food
from constants import *

class FoodField(pygame.sprite.Sprite):
    field = [
        lambda x: x * SNAKE_SIZE + (SNAKE_SIZE-FOOD_SIZE)/2,
        lambda y: y * SNAKE_SIZE + (SNAKE_SIZE-FOOD_SIZE)/2,            
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_count = 0

    def spawn(self, position):
        food = Food(position[0], position[1])

    def update(self, dt, player):
        if self.spawn_count < FOOD_AMOUNT:
            position = (self.field[0](random.randrange(0, SCREEN_WIDTH/SNAKE_SIZE)), self.field[1](random.randrange(0, SCREEN_HEIGHT/SNAKE_SIZE)))
            self.spawn(position)
            self.spawn_count += 1