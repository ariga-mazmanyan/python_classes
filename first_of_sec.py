# class Car:
#     description = "this is car class"
#
#     def __init__(self, name, year, color):
#         self.car_name = name
#         self.car_year = year
#         self.color = color
#
#
# car_1 = Car(name="Maserati", year="2022", color="Black")
# car_2 = Car(name="Mercedes", year="2022", color="White")
# car_3 = Car(name="Mazda", year="2022", color="Red")
#
# print(car_1.car_name, car_1.car_year, car_1.color)


#
# class Cv:
#     description = "this is CV"
#
#     def __init__(self, name, surname, email, age):
#         self.cv_name = name
#         self.cv_surname = surname
#         self.cv_email = email
#         self.cv_age = age
#
#     def present(self):
#         print(f"This is {self.cv_name} {self.cv_surname}")
#
# cv_1 = Cv(name="John", surname="Don", email="johndohn@gmail.com", age="32")
#
# print(cv_1.cv_name, cv_1.cv_surname, cv_1.cv_email, cv_1.cv_age)
# cv_1.present()

class Rectangle:

    def __init__(self, a, b):
        self.first_s = a
        self.second_s = b

    def perimeter(self):
        return 2 * (self.first_s + self.second_s)

    def area(self):
        return self.first_s * self.second_s


rec_1 = Rectangle(10, 20)

print(f"The perimeter of your rectangle is {rec_1.perimeter()} and the area is {rec_1.area()}")










