import turtle


class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float, x: float, y: float, vel_x: float,
                 vel_y: float,
                 color: str) -> None:
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance
        self.__x = x
        self.__y = y
        self.__vel_x = vel_x
        self.__vel_y = vel_y
        self.__t = turtle.Turtle()
        self.__t.color(color)
        self.__t.shape("circle")
        self.__t.penup()
        self.__t.goto(self.__x, self.__y)
        self.__t.pendown()

    def get_mass(self) -> float:
        return self.__mass

    def get_distance(self) -> float:
        return self.__distance

    def get_x_pos(self) -> float:
        return self.__x

    def get_y_pos(self) -> float:
        return self.__y

    def get_vel_x(self) -> float:
        return self.__vel_x

    def get_vel_y(self) -> float:
        return self.__vel_y

    def set_x_vel(self, new_vel_x: float):
        self.__vel_x = new_vel_x

    def set_y_vel(self, new_vel_y: float):
        self.__vel_y = new_vel_y

    def move_to(self, new_x: float, new_y: float):
        self.__x = new_x
        self.__y = new_y
        self.__t.goto(self.__x, self.__y)

    def __str__(self) -> str:
        return f"Planet (name={self.__name}, mass={self.__mass}, x={self.__x}, y={self.__y})"

    def __eq__(self, other):
        return self.__name == other.__name

def main():
    p1 = Planet("Earth,", 5.0, 100, 1000, 1, 1, 500, 100, "Blue")
    p2 = Planet("Earth,", 5.0, 100, 1000, 1, 1, 500, 100, "Blue")
    planets = [p1]
    print(p2 in planets)

if __name__ == '__main__':
    main()