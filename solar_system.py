from sun import Sun
from planet import Planet
import math
from gravity import UniversalGravity as U

class SolarSystem:
    def __init__(self):
        self.the_sun: Sun = None
        self.__planets: list[Planet] = []

    def add_sun(self, the_sun: Sun):
        self.the_sun = the_sun

    def add_planet(self, new_planet: Planet):
        if new_planet not in self.__planets:
            self.__planets.append(new_planet)
        else:
            print("That planet already exists.")

    def show_planets(self):
        for planet in self.__planets:
            print(planet)

    def move_planets(self):
        dt = .001

        for planet in self.__planets:
            planet.move_to(
                planet.get_x_pos() + dt * planet.get_vel_x(),
                planet.get_y_pos() + dt * planet.get_vel_y())

            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x**2 + dist_y**2)

            acc_x = U.G * self.the_sun.get_mass()*dist_x/new_distance**3
            acc_y = U.G * self.the_sun.get_mass()*dist_y/new_distance**3

            planet.set_x_vel(planet.get_vel_x() + dt * acc_x)
            planet.set_y_vel(planet.get_vel_y() + dt * acc_y)