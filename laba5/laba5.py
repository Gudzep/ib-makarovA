import pygame
from pygame.draw import *

pygame.init()
pygame.display.set_caption('Красивый кроль без смс и регистрации')  # кастомное название окна
FPS = 30  # частота кадров

# Цвета
black = (0, 0, 0)
grey = (184, 184, 184)
nedogrey = (120, 104, 104)
bur = (94, 73, 73)
bodyy = (145, 125, 125)
white = (255, 255, 255)

# Разрешение окна по вертикали и горизонтали
screen = pygame.display.set_mode((800, 600))

screen.fill((black))  # заливка фона

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Рэббит получается', 1, (41, 145, 12))  # цвет шрифта

screen.blit(text1, (10, 50))


def draw_body(screen, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(screen, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    '''
    Рисует уши зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует лапы зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_eye(surface, x, y, width, height, color):
    '''
    Рисует глаза зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_os(surface, x, y, width, height, color):
    '''
    Рисует рот зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


# Отрисовка зайца
draw_body(screen, 400, 410, 150, 300, bodyy)  # тело кроля

draw_ear(screen, 360, 100, 40, 200, nedogrey)  # левое ухо
draw_ear(screen, 440, 100, 40, 200, nedogrey)  # правое ухо

draw_head(screen, 400, 200, 150, grey)  # голова кроля

draw_leg(screen, 280, 320, 120, 40, bur)  # левая верхняя лапа
draw_leg(screen, 520, 320, 120, 40, bur)  # правая верхняя лапа

draw_leg(screen, 317, 550, 100, 50, bur)  # левая нижняя лапа
draw_leg(screen, 485, 550, 100, 50, bur)  # правая нижняя лапа

draw_eye(screen, 360, 180, 27, 27, white)  # правый белок глаза
draw_eye(screen, 363, 180, 7, 7, black)  # правый зрачок
draw_eye(screen, 436, 180, 27, 27, white)  # левый белок глаза
draw_eye(screen, 438, 180, 7, 7, black)  # левый зрачок

draw_os(screen, 400, 230, 70, 40, black)  # рот

draw_ear(screen, 397, 218, 5, 15, white)  # левый зуб
draw_ear(screen, 403, 218, 5, 15, white)  # правый зуб

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
