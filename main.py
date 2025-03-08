import pygame
from constants import *
from snake import Snake
from food import Food
from foodfield import FoodField
from score import Score
from tail import Tail
from snaketail import SnakeTail

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.quit()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    foods = pygame.sprite.Group()
    tails = pygame.sprite.Group()

    Snake.containers = (updatable, drawable)
    FoodField.containers = (updatable)
    Food.containers = (drawable, foods)
    Score.containers = (updatable, drawable)
    SnakeTail.containers = (updatable)
    Tail.containers = (updatable, drawable, tails)


    foodfield = FoodField()
    player = Snake(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    playertail = SnakeTail()
    score = Score()

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        updatable.update(dt, player)

        for tail in tails:
            if tail.count == playertail.spawn_count - 1 - playertail.length:
                tail.kill()
                
        player.move(dt)

        if player.position.x < -5 or player.position.x > SCREEN_WIDTH - SNAKE_SIZE +5 or player.position.y < -5 or player.position.y > SCREEN_HEIGHT - SNAKE_SIZE +5:
            score.endscreen(screen)
            pygame.display.update() 
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if pygame.key.name(event.key) == "n":
                            print("Goodbye")
                            exit()
                        if pygame.key.name(event.key) == "y":
                            main()

        for tail in tails:
            if tail.check_for_collision(player):
                score.endscreen(screen)
                pygame.display.update() 
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if pygame.key.name(event.key) == "n":
                                print("Goodbye")
                                exit()
                            if pygame.key.name(event.key) == "y":
                                main()

        for food in foods:
            if food.check_for_collision(player):
                food.kill()
                score.add_points()
                player.length += 1
                playertail.length += 1
                foodfield.spawn_count -= 1

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()