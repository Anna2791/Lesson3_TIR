import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/bamboo.jpg')

target_img = pygame.image.load('img/cucum.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

bamboo_img = pygame.image.load('img/bamboo.jpg')

score = 0
start_time = time.time()
game_duration = 10

font = pygame.font.Font(None, 74)

running = True
game_over = False

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1


    if not game_over and time.time() - start_time >= game_duration:
        game_over = True

    if game_over:
        screen.blit(bamboo_img, (0, 0))
        text = font.render(f"Score: {score}", True, (255, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    else:
        screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

pygame.quit()
