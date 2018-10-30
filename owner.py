from car import Car

class Owner:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def year(self):
        return self._year

    def find_my_cars(self):
        cars_w_name = list(filter(lambda item: item.owner.name == self.name, Car._all))
        return list(map(lambda car: car.make + " " + car.model, cars_w_name))
