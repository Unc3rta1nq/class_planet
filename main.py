from vpython import sphere, vector, color, rotate, canvas
from threading import Thread
import math


# Константы
G = 6.667e-11  # гравитационная постоянная, м^3 кг^-1 с^-2
MSun = 1.9885e30  # масса Солнца, кг
# MEar = 5.97e24  # масса Земли, кг
# MJup = 1.898e27  # масса Юпитера, кг
# MUra = 8.681e25  # масса Урана, кг
# MNep = 1.024e26  # масса Нептуна, кг
# MMer = 3.285e23  # масса Меркурия, кг
# MMar = 6.39e23  # масса Марса, кг
# MSat = 5.683e26  # масса Сатурна, кг
# MVen = 4.867e24  # масса Венеры, кг
# все списки упорядочены по удаленности от солнца
MPlan = [3.285e23, 4.867e24, 5.97e24, 6.39e23, 1.898e27, 5.683e26, 8.681e25,
         1.024e26]  # массы планет
DPlan = [5.8343e10, 1.0771e11, 1.496e11, 2.2739e11, 7.779e11, 1.4272e12, 2.8723e12,
         4.49691e12]  # расстояния от солнца к планете
RPlan = [2439, 6051, 6371, 3389, 69911, 58232, 25362, 24622]  # радиусы планет
# ColorPlan = [vector(128, 128, 128), vector(85, 71, 29), vector(0, 191, 255), vector(188, 134, 11), vector(183, 65, 14),
#              vector(255, 165, 0), vector(48, 71, 72), vector(30, 144, 255)]


# DEar = 1.496e11  # среднее расстояние от Солнца до Земли, метры
# DJup = 7.779e11  # среднее расстояние от Солнца до Юпитера, метры
# DUra = 2.8723e12  # среднее расстояние от Солнца до Урана, метры
# DNep = 4.49691e12  # среднее расстояние от Солнца до Нептуна, метры
# DMer = 5.8343e10  # среднее расстояние от Солнца до Меркурия, метры
# DMar = 2.2739e11  # среднее расстояние от Солнца до Марса, метры
# DSat = 1.4272e12  # среднее расстояние от Солнца до Сатурна, метры
# DVen = 1.0771e11  # среднее расстояние от Солнца до Венеры, метры


class Planet:
    def __init__(self, mass, dist, rad):
        self.mass = mass
        self.dist = dist
        self.ratio = dist / 3.333333e10  # смешное магическое число для норм коэффицентов(расстановка планет на поле)
        self.wp = 0
        self.F = 0
        self.rad = rad / 10000
        self.posx = self.ratio + 7
        self.P = sphere(pos=vector(self.posx, 0, 0), color=color.blue, radius=self.rad, make_trail=True)

    def move_planet(self):
        self.F = G * MSun * self.mass / (self.dist * self.dist)  # Гравитационная сила между Солнцем и планетой, Н
        self.wp = math.sqrt(self.F / (self.mass * self.dist))  # Угловая скорость планеты
        # Будем использовать полярные координаты
        dt = 5  # Шаг
        theta_planet = self.wp * dt  # угол поворота за один шаг:
        while  dt<=10**30:  # Земля и Луна поворачиваются вокруг оси z (0,0,1)
            self.P.pos = rotate(self.P.pos, angle=theta_planet, axis=vector(0, 0, 1))

            dt += 5


scene2 = canvas(title='Example of Solar System',
     width=1900, height=900,
     center=vector(0,0,0), background=color.black)
Sun = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=7)
Mer = Planet(MPlan[0], DPlan[0], RPlan[0])
Ven = Planet(MPlan[1], DPlan[1], RPlan[1])
Ear = Planet(MPlan[2], DPlan[2], RPlan[2])
Mar = Planet(MPlan[3], DPlan[3], RPlan[3])
Jup = Planet(MPlan[4], DPlan[4], RPlan[4])
Sat = Planet(MPlan[5], DPlan[5], RPlan[5])
Ura = Planet(MPlan[6], DPlan[6], RPlan[6])
Nep = Planet(MPlan[7], DPlan[7], RPlan[7])


th1 = Thread(target=Mer.move_planet)
th1.start()
th2 = Thread(target=Ven.move_planet)
th2.start()
th3 = Thread(target=Ear.move_planet)
th3.start()
th4 = Thread(target=Mar.move_planet)
th4.start()
th5 = Thread(target=Mar.move_planet)
th5.start()
th6 = Thread(target=Jup.move_planet)
th6.start()
th7 = Thread(target=Sat.move_planet)
th7.start()
th8 = Thread(target=Ura.move_planet)
th8.start()
th9 = Thread(target=Nep.move_planet)
th9.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
th5.join()
th6.join()
th7.join()
th8.join()
th9.join()