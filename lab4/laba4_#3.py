import pygame
from pygame.draw import *
import numpy as np

pygame.init()

# цвета модели RGB используемые в коде
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (148, 97, 49)
LIGHTBLUE_LAS_1 = (111, 205, 252)
LIGHTBLUE_LAS_2 = (35, 181, 204)
GREEN_BLACK = (4, 138, 1)
PINK_LIGHT = (254, 169, 163)

# ширина и высота картинки
screen = pygame.display.set_mode((800, 800))
screen.fill(WHITE)
FPS = 30


# листва
def draw_foliage(surface, color, x_0, y_0, radius, num):
    abs_x = x_0
    abs_y = y_0
    for i in range(num // 2 + 2):
        circle(surface, color, (x_0 - 20, y_0 + 20), radius)
        circle(surface, BLACK, (x_0 - 20, y_0 + 20), radius, 1)
        x_0 += 10
    x_0 = abs_x
    y_0 = abs_y
    for i in range(num // 2):
        circle(surface, color, (x_0 - 10, y_0), radius)
        circle(surface, BLACK, (x_0 - 10, y_0), radius, 1)
        x_0 += 10
    x_0 = abs_x
    y_0 = abs_y
    for i in range(1):
        circle(surface, color, (x_0, y_0 - 20), radius)
        circle(surface, BLACK, (x_0, y_0 - 20), radius, 1)
        x_0 += 10


# деревья
def draw_tree(surface, x, y, width, height, color, radius_leave, num_leaves):
    rect(surface, BLACK, (x, y, width, height))
    x_0 = x + 10
    y_0 = y - 10
    draw_foliage(surface, color, x_0, y_0, radius_leave, num_leaves)


# облака
def draw_cloud(surface, x_0, y_0, radius):
    abs_x = x_0
    abs_y = y_0
    for i in range(4):
        circle(surface, WHITE, (x_0 - radius, y_0), radius)
        circle(surface, BLACK, (x_0 - radius, y_0), radius, 1)
        x_0 += radius
    x_0 = abs_x
    for i in range(2):
        circle(surface, WHITE, (x_0, y_0 - radius), radius)
        circle(surface, BLACK, (x_0, y_0 - radius), radius, 1)
        x_0 += radius


# дома
def draw_house(surface, x_0, y_0, width, height):
    rect(screen, BROWN, (x_0, y_0, width, height))
    rect(screen, LIGHTBLUE_LAS_2, (x_0 + width // 3, y_0 + height // 3, width // 3, height // 3))
    polygon(screen, RED, [(x_0, y_0), (x_0 + width // 2, y_0 - width // 2), (x_0 + width, y_0)])


# солнце
def draw_sun(surface, x_0, y_0, color, radius):
    phi = 0
    for i in range(360):
        polygon(surface, color, ((x_0 + 5 - int(radius * np.cos(2 * np.pi / 3 - phi)),
                                              y_0 + 5 + int(radius * np.sin(2 * np.pi / 3 - phi))),
                                             (x_0 + 5 + int(radius * np.sin(phi)),
                                              y_0 + 5 - int(radius * np.cos(phi)) // 4),
                                             (x_0 + 5 + int(radius * np.cos(2 * np.pi / 3 + phi)),
                                              y_0 + 5 + int(radius * np.sin(2 * np.pi / 3 + phi)))))
        phi += 10


rect(screen, GREEN, (0, 400, 800, 400))
rect(screen, LIGHTBLUE_LAS_1, (0, 0, 800, 400))

draw_house(screen, 100, 420, 150, 150)
draw_house(screen, 400, 330, 100, 100)

draw_tree(screen, 590, 380, 15, 80, GREEN_BLACK, 25, 6)
draw_tree(screen, 330, 450, 20, 150, GREEN_BLACK, 25, 6)
draw_cloud(screen, 400, 200, 30)
draw_cloud(screen, 600, 250, 20)
draw_cloud(screen, 200, 300, 34)
draw_cloud(screen, 600, 150, 15)
draw_sun(screen, 100, 150, PINK_LIGHT, 70)


# обновляет всю область, как не задан аргумент
pygame.display.flip()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
