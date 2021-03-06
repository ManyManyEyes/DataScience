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
    def __str__(self):
        return f'height:{self.height}\n'\
               f'length:{self.length}\n'\
               f'width:{self.width}\n'\
               f'volume:{self.volume}\n'\
               f'mass:{self.mass}'


class Fridge(Cargo):
    def __str__(self):
        return f'height:{self.height}\n'\
               f'length:{self.length}\n'\
               f'width:{self.width}\n'\
               f'volume:{self.volume}\n'\
               f'mass:{self.mass}'


class Table(Cargo):
    def __str__(self):
        return f'height:{self.height}\n'\
               f'length:{self.length}\n'\
               f'width:{self.width}\n'\
               f'volume:{self.volume}\n'\
               f'mass:{self.mass}'


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
        self._ready_status = True
        self._x = 0
        self._y = 0

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

    @property
    def position(self):
        return self._x, self._y

    @open_door.setter
    def open_door(self, value):
        self._open_door = value

    def check(self, cargo):
        return cargo.height <= self.height and cargo.length <= self.length and cargo.width <= self.width and \
               cargo.volume <= self.volume_available and cargo.mass <= self.carrying_available and \
               self.ready_status is not False

    def load(self, cargo):
        if self.check(cargo) is not False:
            if self.open_door is False:
                self.open_door = True
            self.cargo_list.append(cargo)
            self._carrying_available -= cargo.mass
            self._volume_available -= cargo.volume
            self.open_door = False

    def drop(self, cargo):
        self._carrying_available += cargo.mass
        self._volume_available += cargo.volume
        self.cargo_list.pop()

    def moving(self, x, y):
        self._x += x
        self._y += y


if __name__ == '__main__':
    vagon = Carriage(3, 20, 3, 100000)
    box1 = Box(1, 1, 1, 25)
    box2 = Box.create()
    print(box2)
    vagon.load(box1)
    vagon.load(box2)
    vagon.drop(box1)
    vagon.moving(100, 50)
