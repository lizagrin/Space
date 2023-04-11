from vpython import sphere, vector, color, rotate
import math

G = 6.667e-11  # гравитационная постоянная, м^3 кг^-1 с^-2

#Массы планет, кг
sun_weight = 1.9885e30
earth_weight = 5.97e24
moon_weight = 7.348e22
mars_weight = 6.42e23
venus_weight = 4.87e24
mercury_weight = 3.29e23
saturn_weight = 5.63e26
jupiter_weight = 1.90e27
uranus_weight = 8.68e25
neptune_weight = 1.02e26

#Средние расстояния от Солнца до планет, м
sun_earth_dist = 1.496e11
sun_mars_dist = 2.489e11
sun_venus_dist = 1.075e11
sun_mercury_dist = 5.098e10
sun_saturn_dist = 1.466e12
sun_jupiter_dist = 7.409e11
sun_uranus_dist = 2.939e12
sun_neptune_dist = 4.473e12

# Гравитационные силы между планетами и солнцем, Н
sun_earth_F = G * sun_weight * earth_weight / (sun_earth_dist * sun_earth_dist)
sun_mars_F = G * sun_weight * mars_weight / (sun_mars_dist * sun_mars_dist)
sun_venus_F = G * sun_weight * venus_weight / (sun_venus_dist * sun_venus_dist)
sun_mercury_F = G * sun_weight * mercury_weight / (sun_mercury_dist * sun_mercury_dist)
sun_saturn_F = G * sun_weight * saturn_weight / (sun_saturn_dist * sun_saturn_dist)
sun_jupiter_F = G * sun_weight * jupiter_weight / (sun_jupiter_dist * sun_jupiter_dist)
sun_uranus_F = G * sun_weight * uranus_weight / (sun_uranus_dist * sun_uranus_dist)
sun_neptune_F = G * sun_weight * neptune_weight / (sun_neptune_dist * sun_neptune_dist)

# Угловые скорости
earth_w = math.sqrt(sun_earth_F / (earth_weight * sun_earth_dist))
mars_w = math.sqrt(sun_mars_F / (mars_weight * sun_mars_dist))
venus_w = math.sqrt(sun_venus_F / (venus_weight * sun_venus_dist))
mercury_w = math.sqrt(sun_mercury_F / (mercury_weight * sun_mercury_dist))
saturn_w = math.sqrt(sun_saturn_F / (saturn_weight * sun_saturn_dist))
jupiter_w = math.sqrt(sun_jupiter_F / (jupiter_weight * sun_jupiter_dist))
uranus_w = math.sqrt(sun_uranus_F / (uranus_weight * sun_uranus_dist))
neptune_w = math.sqrt(sun_neptune_F / (neptune_weight * sun_neptune_dist))

v = vector(0.5, 0, 0)
Earth = sphere(pos=vector(9, 0, 0), color=color.green, radius=0.6, make_trail=True)
Sun = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=3)
Mars = sphere(pos=vector(11, 0, 0), color=color.red, radius=0.3, make_trail=True)
Venus = sphere(pos=vector(7, 0, 0), color=color.blue, radius=0.6, make_trail=True)
Mercury = sphere(pos=vector(5, 0, 0), color=color.orange, radius=0.5, make_trail=True)
Saturn = sphere(pos=vector(31, 0, 0), color=color.white, radius=2.1, make_trail=True)
Jupiter = sphere(pos=vector(20, 0, 0), color=color.cyan, radius=1.7, make_trail=True)
Uranus = sphere(pos=vector(66, 0, 0), color=color.purple, radius=1, make_trail=True)
Neptune = sphere(pos=vector(100, 0, 0), color=color.magenta, radius=1, make_trail=True)

# Будем использовать полярные координаты
# Шаг
dt = 10

# углы поворота за один шаг:
theta_earth = earth_w * dt
theta_mars = mars_w * dt
theta_venus = venus_w * dt
theta_mercury = mercury_w * dt
theta_saturn = saturn_w * dt
theta_jupiter = jupiter_w * dt
theta_uranus = uranus_w * dt
theta_neptune = neptune_w * dt
while dt <= 86400 * 365:
    #Поворот вокруг оси z (0,0,1)
    Earth.pos = rotate(Earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
    Mars.pos = rotate(Mars.pos, angle=theta_mars, axis=vector(0, 0, 1))
    Venus.pos = rotate(Venus.pos, angle=theta_venus, axis=vector(0, 0, 1))
    Mercury.pos = rotate(Mercury.pos, angle=theta_mercury, axis=vector(0, 0, 1))
    Saturn.pos = rotate(Saturn.pos, angle=theta_saturn, axis=vector(0, 0, 1))
    Jupiter.pos = rotate(Jupiter.pos, angle=theta_jupiter, axis=vector(0, 0, 1))
    Uranus.pos = rotate(Uranus.pos, angle=theta_uranus, axis=vector(0, 0, 1))
    Neptune.pos = rotate(Neptune.pos, angle=theta_neptune, axis=vector(0, 0, 1))
dt += 10
