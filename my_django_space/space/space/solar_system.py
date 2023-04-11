import csv


class Planet:
    def __init__(self, name, diameter, mass, inclination, eccentricity, gravity, orbitalPeriod, siderealRotation,
                 satellites):
        self.name = name
        self.diameter = diameter
        self.mass = mass
        self.inclination = inclination
        self.eccentricity = eccentricity
        self.gravity = gravity
        self.orbitalPeriod = orbitalPeriod
        self.siderealRotation = siderealRotation
        self.satellites = satellites


planets = {}
names = []
with open("information/planets.csv", encoding='utf-8') as r_planets:
    heading = next(r_planets)
    file_reader = csv.reader(r_planets, delimiter=',')
    count = 0
    for row in file_reader:
        names.append(row[0])
        planets[names[count]] = Planet(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        count += 1
    print(planets['Mercury'].name, planets['Venus'].diameter)
