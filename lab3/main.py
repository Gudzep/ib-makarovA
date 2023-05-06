import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 900))
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

circle(screen, (255, 251, 0), (450, 450), 300)
circle(screen, (255, 0, 0), (300, 400), 50)
circle(screen, (0, 0, 0), (300, 400), 20)
circle(screen, (255, 0, 0), (625, 400), 40)
circle(screen, (0, 0, 0), (625, 400), 17)

line(screen, BLACK, (150, 150), (400, 400), 40)
line(screen, YELLOW, (260, 150), (240, 130), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()