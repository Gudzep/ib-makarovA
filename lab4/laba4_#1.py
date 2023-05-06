import pygame
from pygame.draw import *

pygame.init()


FPS = 30
screen = pygame.display.set_mode((900, 900))
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
hh = (184, 182, 182)

screen.fill(hh)

circle(screen, yellow, (450, 450), 300)
circle(screen, black, (450, 450), 300, 2)
# глаза
circle(screen, red, (300, 400), 50)
circle(screen, black, (300, 400), 50, 2)
circle(screen, black, (300, 400), 20)
circle(screen, red, (625, 400), 40)
circle(screen, black, (625, 400), 17)
circle(screen, black, (625, 400), 40, 2)
# брови
line(screen, black, (150, 190), (400, 400), 40)
line(screen, black, (720, 256), (547, 390), 40)
# рот
line(screen, black, (300, 600), (600, 600), 40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
