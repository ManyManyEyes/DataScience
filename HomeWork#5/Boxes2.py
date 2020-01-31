import random


def gen(a, b):
    return random.uniform(a, b)


class Box:
    def __init__(self, height, length, width, mass):
        self._height = height
        self._length = length
        self._width = width
        self._mass = mass
        self._volume = height * length * width

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
        self._volume = height * length * width
        self.storage = []
        self.status = closed

        
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
    
    
    def check(self, cargo):
        if cargo.height <= self.height
            if cargo.length <= self.length
                if cargo.width <= self.width

    def load(self, load):
        if self.volume < load.volume or self.carrying < load.mass:
            print(
                f"The box {i} will not fit: box {load.volume or load.mass}, remaining in the carriage {self.volume or self.carrying}")
            exit()
        else:
            self.volume = self.volume - load.volume
            self.carrying = self.carrying - load.mass
            self.storage.append(load)
            print(f"""The box {i} is shipped. Box parameters: 
            height: {load.height} 
            weight: {load.width}
            length: {load.length} 
            volume: {load.volume}
            mass: {load.mass}
            Left volume in the carriage {self.volume}, left carrying in the carriage {self.carrying}
            Boxes in carriage: {len(self.storage)}""")


if __name__ == '__main__':
    Box.create
    Box.create()

