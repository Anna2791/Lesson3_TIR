import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGT = 600
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGT))
pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/0000978_moorhuhn-crazy-chicken-digital-version-.jpg')

target_img = pygame.image.load('img/target.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)

color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))



running = True
while running:
    pass
pygame.quit()
