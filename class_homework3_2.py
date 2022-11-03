class Hotel:
    def __init__(self, hotel_name, hotel_place, mid_room_price, lux_room_price, *args, **kwargs):
        self.hname = hotel_name
        self.hplace = hotel_place
        self.mid_price = mid_room_price
        self.lux_price = lux_room_price
        self.room_mid = {1: "free", 2: "free", 3: "free"}
        self.room_lux = {4: "free", 5: "free", 6: "free"}
        super().__init__(*args, **kwargs)

    def present(self):
        return f"Our {self.hname} is situated on {self.hplace}"

    def booking(self, a):

        room_mid = [i for i in self.room_mid]
        room_lux = [i for i in self.room_lux]

        if a in room_mid and self.room_mid[a] == "free":
            self.room_mid[a] = "busy"
        elif a in room_lux and self.room_lux[a] == "free" :
            self.room_lux[a] = "busy"
        else:
            return "busy"

    def discount(self, room_num, discount):

        room_mid = [i for i in self.room_mid]

        if room_num in room_mid:
            new_price = self.mid_price - (self.mid_price * discount) / 100
        else:
            new_price = self.mid_price - (self.mid_price * discount) / 100

        return new_price


class Taxi:
    def __int__(self, taxi_name, car_types, price_for_tour, *args, **kwargs):
        self.taxi_name = taxi_name
        self.car_types = car_types
        self.tour_price = price_for_tour
        super().__init__(*args, **kwargs)

    def present(self):
        return f"Our taxi service {self.taxi_name} has {self.car_types} for your comfortable tours. The price for" \
               f" the tour is {self.tour_price}"

    def discount(self, a):
        new_price = self.tour_price - (self.tour_price * a) / 100

        return new_price


class Tour(Hotel, Taxi):
    def __init__(self, tour_name, tour_price, *args, **kwargs):
        self.tour_name = tour_name
        self.tour_price = tour_price
        self.price_mid_tour = self.mid_price + self.tour_price
        self.price_lux_tour = self.lux_price + self.tour_price
        super().__init__(*args, **kwargs)

    def global_presentation(self):
        return f"We are offering {self.tour_name} tour. We will stay at {self.hname} where you have two options to" \
               f"choose from Lux room({self.price_lux_tour}) and Mid room({self.price_mid_tour}) which includes a " \
               f"transport {self.taxi_name} taxi and they provide {self.car_types} car."


tour_1 = Tour(tour_name="Geghard", hotel_name="Lerane", lux_room_price=50000, mid_room_price=30000, taxi_name="ride_over",
              car_types="mercedes", price_for_tour=10000, hotel_place="Geghard", tour_price=10000)

print(tour_1.global_presentation())