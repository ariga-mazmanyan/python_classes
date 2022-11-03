class Country:
    def __init__(self, country_name, continent, *args, **kwargs):
        self.cname = country_name
        self.cont = continent
        super().__init__(*args, **kwargs)

    def present(self):
        return f"{self.cname} is in {self.cont}"


class Brand:
    def __init__(self, business_name, start_date, *args, **kwargs):
        self.bname = business_name
        self.startdate = start_date
        super().__init__(*args, **kwargs)

    def present(self):
        return f"The {self.bname} is created on {self.startdate}"


class Season:
    def __init__(self, season_name, av_temp):
        self.sname = season_name
        self.avtemp = av_temp


class Product(Country, Brand, Season):
    def __init__(self, product_name, product_type, product_price, product_quantity, *args, **kwargs):
        self.pname = product_name
        self.type = product_type
        self.price = product_price
        self.quantity = product_quantity
        super().__init__(*args, **kwargs)

    def present(self):
        return f"The {self.pname} is made by {self.bname} crated on {self.startdate} in {self.cname}." \
               f"Our product is {self.type} and costs {self.price}. " \
               f"Higest sales are in {self.sname}"

    def discount(self, a):

        new_price = self.price - (self.price * a) / 100

        return new_price

    def increase_quantity(self, b):

        new_quantity = self.quantity + b

        return new_quantity

    def decrease_quantity(self, c):

        new_quantity = self.quantity - c

        return new_quantity


product_1 = Product("Samsung technologies", "phone", 400000, 100, country_name="Korea", continent="Asia",
                    business_name="Samsung", season_name="Winter", start_date = "1969 01 13", av_temp = 27)

print(product_1.present())



