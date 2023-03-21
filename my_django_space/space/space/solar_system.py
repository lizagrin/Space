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


mercury, venus, earth, mars, jupiter, saturn, uranus, neptune = Planet, Planet, Planet, Planet, Planet, Planet, Planet, Planet
with open("information/planets.csv", encoding='utf-8') as r_planets:
    heading = next(r_planets)
    file_reader = csv.reader(r_planets, delimiter=',')
    count = 0

    for row in file_reader:
        if count == 0:
            mercury.name = row[0]
            mercury.diameter = row[1]
            mercury.mass = row[2]
            mercury.inclination = row[3]
            mercury.eccentricity = row[4]
            mercury.gravity = row[5]
            mercury.orbitalPeriod = row[6]
            mercury.siderealRotation = row[6]
            mercury.satellites = row[7]
        count += 1
    print(mercury.name, mercury.diameter, mercury.mass, mercury.inclination, mercury.eccentricity, mercury.gravity, mercury.orbitalPeriod, mercury.siderealRotation, mercury.satellites)