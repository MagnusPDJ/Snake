import pygame

# Base class for game objects
class SquareShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.width = width
        self.height = height

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt, player):
        # sub-classes must override
        pass

    def check_for_collision(self, player):
        return pygame.Rect(self.position.x, self.position.y, self.width, self.height).colliderect(
            pygame.Rect(player.position.x, player.position.y, player.width, player.height))