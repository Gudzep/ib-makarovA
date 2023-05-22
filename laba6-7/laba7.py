import pygame
import math
from pygame.draw import *
from random import randint

pygame.init()
pygame.display.set_caption('Пау-пиу')
FPS = 60
screen = pygame.display.set_mode((1280, 720))
score = 0
desired_score = 60  # количество очков для победы
game_duration = 50  # время для возможности играть

start_time = pygame.time.get_ticks()  # запуск времени
elapsed_time = 0

x = randint(100, 700)
y = randint(100, 500)
v1 = [-1, 1]
vx = v1[randint(0, 1)]
vy = v1[randint(0, 1)]

maxx = 1280
maxy = 720
sum = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

a = randint(2, 6)

pos_x = []
for i in range(a):
    pos_x.append(0)
    pos_x[i] = randint(100, 700)

pos_y = []
for i in range(a):
    pos_y.append(0)
    pos_y[i] = randint(100, 700)

pos_r = []
for i in range(a):
    pos_r.append(0)
    pos_r[i] = randint(30, 100)
color = []
for i in range(a):
    color.append(0)
    color[i] = COLORS[randint(0, 5)]
main_paramsmass = []
for i in range(a):
    main_paramsmass.append(0)
    main_paramsmass[i] = [pos_x[i], pos_y[i], vx + 10 * i, vy + 10 * i, color[i]]


def click(event):
    global x, y, r
    print(x, y, r)


def score(sum):
    font = pygame.font.Font(None, 25)
    text = font.render('Твой счет: ' + str(sum), 1, (255, 255, 255))
    screen.blit(text, (1100, 10))


def timer():
    font = pygame.font.Font(None, 25)
    time_elapsed = pygame.time.get_ticks() - start_time
    seconds = (game_duration * 1000 - time_elapsed) // 1000
    text = font.render('Оставшееся время: ' + str(seconds), 1, (255, 255, 255))
    screen.blit(text, (10, 10))


clock = pygame.time.Clock()
finished = False


def ball(x, y, r, color, vx, vy):
    x += vx
    y += vy
    clock.tick(FPS)
    if x >= (1280 - r):
        vx *= (-1)
    elif x <= (0 + r):
        vx *= (-1)
    if y >= (720 - r):
        vy *= (-1)
    elif y <= (0 + r):
        vy *= (-1)
    circle(screen, color, (x, y), r)
    return [x, y, vx, vy, color]


vxs = v1[randint(0, 1)]
vys = vxs
main_paramss = [randint(100, 700), randint(100, 700), randint(80, 160), randint(80, 160), vxs, vys,
                COLORS[randint(0, 5)]]


def squar(x, y, w, h, vxs, vys, color):
    x += vxs
    y += 20 * vys * math.cos(x * vxs / 10)
    clock.tick(FPS)
    if x >= (1280 - w):
        vxs *= (-1)
    elif x <= 0:
        vxs *= (-1)
    if y >= (720 - h):
        vys *= (-1)
    elif y <= 0:
        vys *= (-1)
    rect(screen, color, (x, y, w, h))
    return [x, y, w, h, vxs, vys, color]


while not finished:
    click = False

    while click == False and finished == False:
        for i in range(len(main_paramsmass)):
            main_paramsmass[i] = ball(main_paramsmass[i][0], main_paramsmass[i][1], pos_r[i], main_paramsmass[i][4],
                                      main_paramsmass[i][2], main_paramsmass[i][3])
            score(sum)
        main_paramss = squar(main_paramss[0], main_paramss[1], main_paramss[2], main_paramss[3], main_paramss[4],
                             main_paramss[5], COLORS[randint(0, 5)])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Даб-даб клик')
                for i in range(len(main_paramsmass)):
                    if (main_paramsmass[i][0] - event.pos[0]) ** 2 + (main_paramsmass[i][1] - event.pos[1]) ** 2 <= \
                            pos_r[i] ** 2:
                        main_paramsmass[i] = [randint(100, 700), randint(100, 500), v1[randint(0, 1)],
                                              v1[randint(0, 1)], COLORS[randint(0, 5)]]
                        sum += 1
                        print('счет ', sum)
                        click = True
                if event.pos[0] <= (main_paramss[0] + main_paramss[2]) and event.pos[0] >= main_paramss[0] and \
                        event.pos[1] >= main_paramss[1] and event.pos[1] <= main_paramss[1] + main_paramss[3]:
                    main_paramss[4] *= (2)
                    sum += 3
                    print('счет ', sum)
                    click = True
        if sum >= desired_score:
            finished = True

        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        if elapsed_time >= game_duration:
            finished = True

        timer()  # обновляет время на дисплее

        pygame.display.update()
        screen.fill(BLACK)
print('Игра завершена! Твой итоговый счет:', sum)
pygame.quit()
toplist = []
print('Введите свой ник пжпжпж:'
      '')
nick = input()
f = open(r'C:\Users\skmemes\ib-makarovA\best_players.txt', 'r')
for line in f:
    toplist.append(line)
toplist.append(str((nick, sum)))
f.close()
f = open(r'C:\Users\skmemes\ib-makarovA\best_players.txt', 'w')
for i in range(len(toplist)):
    f.write(toplist[i])
f.close()
f = open(r'C:\Users\skmemes\ib-makarovA\best_players.txt', 'r')
for line in f:
    print(line)