import random


def gen(a, b):
    return random.uniform(a, b)


class Box:
    def __init__(self, height, length, width, mass):
        self._height = height
        self._length = length
        self._width = width
        self._mass = mass
        self._volume = height*length*width


    @property
    def height(self):
        return self._height
    def length(self):
        return self._length
    def width(self):
        return self._width
    def mass(self):
        return self._mass
    def volume(self):
        return self._volume


    @classmethod
    def create(cls):
        self._height = gen
        self._length = gen
        self._width = gen
        self._mass =
        self._volume = 


class Carriage:
    def __init__(self, height, length, width, carrying):
        self._height = height
        self._length = length
        self._width = width
        self._carrying = carrying
        self._volume = height*length*width
        self.storage = []
        self.status = closed

        @property
    def height(self):
        return self._height
    def length(self):
        return self._length
    def width(self):
        return self._width
    def carrying(self):
        return self._carrying
    def volume(self):
        return self._volume


    def check(self,cargo):

    def load(self, load):
        if self.volume < load.volume or self.carrying < load.mass:
            print(f"The box {i} will not fit: box {load.volume or load.mass}, remaining in the carriage {self.volume or self.carrying}")
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
    vagon = Carriage()
    for i in range(1, 11):
        vagon.load(Box())
