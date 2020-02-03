import random


def gen(a, b):
    return random.uniform(a, b)


class Cargo:
    def __init__(self, height, length, width, mass):
        self._height = height
        self._length = length
        self._width = width
        self._mass = mass
        self._volume = self._height * self._length * self._width

    @classmethod
    def create(cls):
        height = gen(0.1, 3.0)
        length = gen(0.1, 10.0)
        width = gen(0.1, 3.0)
        volume = height * length * width
        mass = volume * gen(1.0, 3.0)
        cargo = cls(height, length, width, mass, volume)
        return cargo

    @property
    def height(self):
        return self._height
    @property
    def length(self):
        return self._length
    @property
    def width(self):
        return self._width
    @property
    def volume(self):
        return self._volume
    @property
    def mass(self):
        return self._mass


class Carriage:
    def __init__(self, height, length, width, carrying):
        self._height = height
        self._length = length
        self._width = width
        self._carrying = carrying
        self._volume = self._height * self._length * self._width
        self.carrying_available = self._carrying
        self.volume_available = self._volume
        self.cargo_list = []
        self.storage_list = []

        
    @property
    def height(self):
        return self._height
    @property
    def length(self):
        return self._length
    @property
    def width(self):
        return self._width
    @property
    def carrying(self):
        return self._carrying
    @property
    def volume(self):
        return self._volume
    @property
    def carrying_available(self):
        return self.carrying_available
    @property
    def volume_available(self):
        return self.volume_available
    @property
    def cargo_list(self):
        return self.cargo_list
    @property
    def storage_list(self):
        return self.storage_list
    
    
    def check(self, cargo):
        if cargo._height >= self.height\
        or cargo._length >= self.length\
        or cargo._width >= self.width\
        or cargo._volume >= self._volume_available\
        or cargo._mass >=self._carrying_available:
            return False
        else:
            return True
                    
    def load(self, cargo):
        if self.check(cargo) is not False:
            self.cargo_list.append(cargo)
            self._carrying_available-=cargo._mass
            self._volume_available-=cargo._volume
        else:
            self.storage_list.append(cargo)

    def drop(self, cargo):
        self._carrying_available+=cargo._mass
        self._volume_available+=cargo._volume
        cargo = self._cargo_list.pop
        self._storage_list.append(cargo)


if __name__ == '__main__':

    Box = Cargo(5,5,5,125)
    Vagon = Carriage(10,10,10,100)
    Vagon.load(Box)
    Vagon.drop(Box)
