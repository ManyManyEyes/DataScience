import random


def gen(a, b):
    return random.uniform(a, b)
storage_list = []

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
        return cls(height, length, width, mass)

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

class Box(Cargo):
    def info(self,cls):
        print(f'height:{self.height}',
              f'length:{self.length}',
              f'width:{self.width}',
              f'volume:{self.volume}',
              f'mass:{self.mass}')
        
class Fridge(Cargo):
    def info(self):
        print(f'height:{self._height}',
              f'length:{self._length}',
              f'width:{self._width}',
              f'volume:{self._volume}',
              f'mass:{self._mass}')
    
class Table(Cargo):
    def info(self):
        print(f'height:{self._height}',
              f'length:{self._length}',
              f'width:{self._width}',
              f'volume:{self._volume}',
              f'mass:{self._mass}')
    
class Carriage:
    def __init__(self, height, length, width, carrying):
        self._height = height
        self._length = length
        self._width = width
        self._carrying = carrying
        self._volume = self._height * self._length * self._width
        self._carrying_available = self._carrying
        self._volume_available = self._volume
        self._cargo_list = []
        self._open_door = False
        self._ready_status = False

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
        return self._carrying_available

    @property
    def volume_available(self):
        return self._volume_available

    @property
    def cargo_list(self):
        return self._cargo_list

    @property
    def open_door(self):
        return self._open_door

    @property
    def ready_status(self):
        return self._ready_status


    def check(self, cargo):
        return cargo.height <= self.height and cargo.length <= self.length and cargo.width <= self.width and \
               cargo.volume <= self.volume_available and cargo.mass <= self.carrying_available

    def load(self, cargo):
        if self.check(cargo) is not False:
            self.cargo_list.append(cargo)
            self._carrying_available -= cargo.mass
            self._volume_available -= cargo.volume


    def drop(self, cargo):
        self._carrying_available += cargo.mass
        self._volume_available += cargo.volume
        cargo = self.cargo_list.pop


if __name__ == '__main__':
    Box1 = Box(5, 5, 5, 25)
    Box1.info
    Box1.info(Box(5,5,5,25))
    Vagon = Carriage(10, 10, 10, 100)
