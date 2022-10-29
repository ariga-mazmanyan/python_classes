class Dict1:

    def __init__(self, string_):

        new_dict = dict()
        for i in string_:
            new_dict[i] = string_.count(i)

        self.dict = new_dict

    def remove_dup_val(self):

        list_of_val = []
        dict_without_dup = dict()

        for i, j in self.dict.items():
            if j not in list_of_val:
                dict_without_dup[i] = j
                list_of_val.append(j)

        return dict_without_dup

    def high_vals_in_dict(self):

        list_vals = []
        for i in self.dict.values():
            if i not in list_vals:
                list_vals.append(i)

        list_vals.sort()
        return list_vals[-1], list_vals[-2], list_vals[-3]


string = Dict1("aaaabcrrrdabcfcr")
print(string.remove_dup_val())
print(string.high_vals_in_dict())


# 2
class Circle:

    def __init__(self, radius):
        self.r = radius

    def perimeter_of_circle(self):
        return 2 * 3.14 * self.r

    def area_of_circle(self):
        return 3.14 * self.r ** 2


circle_rad = Circle(10)
print(circle_rad.perimeter_of_circle())
print(circle_rad.area_of_circle())
