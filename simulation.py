import turtle
from time import sleep
from sun import Sun
from planet import Planet
from solar_system import SolarSystem


class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self.__solar_system = solar_system
        self.__width = width
        self.__height = height
        self.__num_periods = num_periods
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width=self.__width, height=self.__height)
        self.__screen.bgcolor("black")
        self.__t.clear()

    def run(self):
        self.__solar_system.show_planets()
        for a_move in range(self.__num_periods):
            self.__solar_system.move_planets()
            self.__solar_system.show_planets()
            #sleep(.1)
        self.freeze()

    def freeze(self):
       self.__screen.exitonclick()

if __name__ == '__main__':
    solar_system = SolarSystem()
    simulation = Simulation(solar_system, width=500, height=500, num_periods=2000)

    sol = Sun("Sol", 5000, 1000000000000000, 5800, 0, 0)

    solar_system.add_sun(sol)

    earth = Planet("Earth", 50, 100, 70, 0, 75, 20, 0, "Blue")
    solar_system.add_planet(earth)

    simulation.run()
