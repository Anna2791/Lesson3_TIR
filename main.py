import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGT = 600
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/bamboo.jpg')

target_img = pygame.image.load('img/cucum.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGT - target_height)
color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))



running = True
while running:
    pass
pygame.quit()


