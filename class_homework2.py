class Human:

    def __init__(self, name, surname, age, height, weight, gender):
        self.n = name
        self.s = surname
        self.a = age
        self.h = height
        self.w = weight
        self.g = gender

    def hundred_years(self):

        age_100 = 100 - self.a + 2022

        return age_100

    def optimal_weight(self):

        if self.g == "male":
            opt_w = int(50 + (0.91 * self.h - 152.4))
        else:
            opt_w = int(45.5 + (0.91 * self.h - 152.4))

        return opt_w

    def present(self):
        print(f"The person is {self.g}. The full name is {self.n} {self.s}, age is {self.a},"\
              f"the height and the weight are {self.h}cm and {self.w} kg")


class Student(Human):
    def __init__(self, name, surname, age, weight, height, marks: list, gender, uni):
        Human.__init__(self, name, surname, age, weight, height, gender)
        self.marks = marks
        self.g = gender
        self.uni = uni

    def add_marks(self, new_mark):
        self.nm = new_mark
        self.marks.append(self.nm)

        print(self.marks)

    def average_mark(self):

        m = 0

        for i in self.marks:
            m += i

        av_mark = m / len(self.marks)

        return av_mark

    def student_description(self):
        if self.g.lower() == "male":
            print(f"{self.n} {self.s} is a {self.a} years old student from {self.uni}. His height is "
                  f"{self.h} with a weight {self.w}. His marks are {self.marks}")
        else:
            print(f"{self.n} {self.s} is a {self.a} years old student from {self.uni}. Her height is "
                  f"{self.h} with a weight {self.w}. Her marks are {self.marks}")


student = Human("David", "Grigoryan", 19, 184, 67, "male")
print(f"You'll turn 100 in {student.hundred_years()}")
print(f"Your optimal weight is {student.optimal_weight()}")
student.present()

marks = [20, 20, 19, 18, 20]
student = Student("David", "Grigoryan", 19, 184, 67, marks, "male", "YSU")
student.add_marks(int(input("Add new mark: ")))
print(f"The average mark is {student.average_mark()}")
student.student_description()
