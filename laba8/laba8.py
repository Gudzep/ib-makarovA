from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

g = 0.5
minspeed = 0.000001
tension = 0.5


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x < self.r and self.vx < 0:
            self.vx = -self.vx
        if self.x > 800 - self.r and self.vx > 0:
            self.vx = -self.vx * tension
        if self.y > 600 - self.r and self.vy > 0:
            self.vy = -self.vy * tension
            if abs(self.vx) <= minspeed:
                self.vx = 0
            else:
                self.vx -= (abs(self.vx) / self.vx) * tension

        self.x += self.vx
        self.y += self.vy
        self.vy += g
        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        hit = False
        r = (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2
        if r < ((self.r + obj.r) ** 2):
            hit = True
        return hit


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        if self.x < self.r and self.vx < 0:
            self.vx = -self.vx
        if self.x > 800 - self.r and self.vx > 0:
            self.vx = -self.vx
        if self.y < self.r and self.vy < 0:
            self.vy = -self.vy
        if self.y > 600 - self.r and self.vy > 0:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        self.vy += g
        self.set_coords()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)
        self.vx = rnd(2, 10)
        self.vy = rnd(2, 10)
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        canv.itemconfig(self.id_points, text=points)


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global text_time1, text_time2, t1, t2, screen1, balls, bullet, all_points
    t1.new_target()
    t2.new_target()
    all_points = 0
    bullet = 0
    text_time1 = 0
    text_time2 = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    while t1.live or balls or t2.live:

        for b in balls:
            b.move()
            if text_time1 == 0 and text_time2 == 0:
                if b.hittest(t1) and t1.live > 0:
                    all_points += 1
                    t1.live = 0
                    text_time1 = 100
                    t1.hit(all_points)
                    canv.itemconfig(t2.id_points, text="")
                    canv.itemconfig(t2.id_points, text=all_points)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    bullet = 0
                if b.hittest(t2) and t2.live > 0:
                    all_points += 1
                    t2.live = 0
                    text_time2 = 100
                    t2.hit(all_points)
                    canv.itemconfig(t1.id_points, text="")
                    canv.itemconfig(t1.id_points, text=all_points)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    bullet = 0

            if b.vx ** 2 + b.vy ** 2 < 1:
                canv.delete(b.id)
                balls.remove(b)
        if text_time1 > 0:
            text_time1 -= 1
            if text_time1 == 1:
                t1.new_target()
        else:
            if text_time2 > 0:
                text_time2 -= 1
                if text_time2 == 1:
                    t2.new_target()
            else:
                t1.move()
                t2.move()
                canv.bind('<Button-1>', g1.fire2_start)
                canv.bind('<ButtonRelease-1>', g1.fire2_end)
                canv.itemconfig(screen1, text='')

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

root.mainloop()