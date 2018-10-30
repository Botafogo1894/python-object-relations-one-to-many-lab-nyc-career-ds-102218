class Car:
    _all = []

    def __init__(self, make, model, year, owner = None):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)
        #remember to associate a car with its owner

    @property
    def make(self):
        return self._make
    @property
    def model(self):
        return self._model
    @property
    def year(self):
        return self._make
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, person):
        self._owner = person
