import math

class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled: bool=False):
        self.__color = list(__color)
        self.filled = filled
        self.__sides = []

        if self.__is_valid_sides(__sides):
            self.__sides = list(__sides)
        else:
            for i in range(0, self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        new_color = []

        if self.__is_valid_color(r, g, b):
            new_color.append(r)
            new_color.append(g)
            new_color.append(b)
            self.__color = new_color

    def __is_valid_sides(self, args):
        count_sides = 0

        for i in args:
            if isinstance(i, int):
                if i > 0 and count_sides < self.sides_count:
                    count_sides += 1
                else:
                    return False
            else:
                return False

        if count_sides == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    #периметр
    def __len__(self):
        len = 0
        for side in self.__sides:
            len += side

        return len

    def set_sides(self, *new_sides):
        list_sides = []

        if self.__is_valid_sides(new_sides):
            for side in new_sides:
                list_sides.append(side)
            self.__sides = list_sides

class Circle(Figure):
    def __init__(self, __color, *__sides, filled: bool = False):
        super().__init__(__color, *__sides, filled=filled)
        self.__radius = self.__len__() / (2 * 3.141569)

    sides_count = 1

    def get_square(self):
        return (self.__radius ** 2) * 3.141569


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        square = self.__len__()
        for side in self.__sides:
            square *= self.__len__() - side

        return math.sqrt(square)

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides, filled: bool = False):
        super().__init__(__color)
        self.__sides = []
        __color = list(__color)
        self.filled=filled

        if self.__is_valid_sides(__sides):
            for i in range(1, self.sides_count):
                self.__sides.append(__sides[0])
        else:
            for i in range(1, self.sides_count):
                self.__sides.append(1)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, args):
        list1 = list(args)
        count_sides = 0

        for i in list1:
                if i > 0 and count_sides < 1 and isinstance(i, int):
                    count_sides += 1
                else:
                    return False

        if count_sides == 1:
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        list_sides = []

        if self.__is_valid_sides(new_sides):
            for i in range(1,12):
                list_sides.append(new_sides)
            self.__sides = list_sides

    def get_volume(self):
        return self.__sides[0] ** 3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())