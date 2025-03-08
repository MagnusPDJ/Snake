import pygame
from tail import Tail
from constants import *

class SnakeTail(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.length = SNAKE_LENGTH
        self.spawn_count = 0
        self.turn_timer = 0

    def spawn(self, position, count):
        tail = Tail(position.x, position.y, count)

    def update(self, dt, player):
        if self.turn_timer > 0:
            self.turn_timer -= dt * SNAKE_SPEED * (1 + (self.length//10))
            if self.turn_timer <0:
                self.turn_timer = 0


        if self.turn_timer > 0:
            return
        self.spawn(player.position, self.spawn_count)
        self.spawn_count += 1
        self.turn_timer = 1