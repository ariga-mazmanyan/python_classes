import math as m


class Triangle:
    count = 0

    def __new__(cls, *args, **kwargs):
        cls.count += 1

        return super().__new__(cls)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.list = [self.a, self.b, self.c]

    def __eq__(self, other):
        return all(item in self.list for item in other.list)

    def area(self):
        p = (self.a + self.b + self.c)/2
        return m.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimetr(self):
        return self.a + self.b + self.c


class Rectangular:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.list = [self.a, self.b]

    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        return all(item in self.list for item in other.list)

    def __gt__(self, other):
        if self.a > other.a or self.a > other.b:
            if self.b > other.a or self.b > other.b:
                return True
        else:
            return False


t_1 = Triangle(3, 4, 5)
t_2 = Triangle(4, 5, 3)

print(t_1 == t_2)

rectangular_1 = Rectangular(10, 7)
rectangular_2 = Rectangular(5, 4)

print(rectangular_1 == rectangular_2)
print(rectangular_1 > rectangular_2)


