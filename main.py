from vpython import sphere, vector, color, rotate
from threading import Thread
import math

# Константы
G = 6.667e-11  # гравитационная постоянная, м^3 кг^-1 с^-2
MSun = 1.9885e30  # масса Солнца, кг
MEar = 5.97e24  # масса Земли, кг
MJup = 1.898e27  # масса Юпитера, кг
MUra = 8, 681e25  # масса Урана, кг
MNep = 1.024e26  # масса Нептуна, кг
MMer = 3.285e23  # масса Меркурия, кг
MMar = 6.39e23  # масса Марса, кг
MSat = 5.683e26  # масса Сатурна, кг
MVen = 4.867e24  # масса Венеры, кг
DEar = 1.496e11  # среднее расстояние от Солнца до Земли, метры
DJup = 7.779e11  # среднее расстояние от Солнца до Юпитера, метры
DUra = 2.8723e12  # среднее расстояние от Солнца до Урана, метры
DNep = 4.49691e12  # среднее расстояние от Солнца до Нептуна, метры
DMer = 5.8343e10  # среднее расстояние от Солнца до Меркурия, метры
DMar = 2.2739e11  # среднее расстояние от Солнца до Марса, метры
DSat = 1.4272e12  # среднее расстояние от Солнца до Сатурна, метры
DVen = 1.0771e11  # среднее расстояние от Солнца до Венеры, метры
delta_dist = 3


class Planet:
    def __init__(self, mass, dist, delta_dist):
        self.mass = mass
        self.dist = dist
        self.wp = 0
        self.F = 0
        self.P = sphere(pos=vector(delta_dist, 0, 0), color=color.blue, radius=.25, make_trail=True)
        self.v = vector(0.5, 0, 0)

    def move_planet(self):
        self.F = G * MSun * self.mass / (self.dist * self.dist)  # Гравитационная сила между Солнцем и планетой, Н
        self.wp = math.sqrt(self.F / (self.mass * self.dist))  # Угловая скорость планеты
        # Будем использовать полярные координаты
        dt = 10  # Шаг
        theta_planet = self.wp * dt  # угол поворота за один шаг:
        while True:  # Земля и Луна поворачиваются вокруг оси z (0,0,1)
            self.P.pos = rotate(self.P.pos, angle=theta_planet, axis=vector(0, 0, 1))
            dt += 10


Sun = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=1)
Merc = Planet(MMer, DMer)
delta_dist += 3
start_new_thread(Merc.move_planet,())
Earth.move_planet()
for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()