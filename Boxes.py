import random


def gen(a, b):
    return random.uniform(a, b)


class Box:
    def __init__(self):
        self.height = gen(0.1, 3.0)
        self.width = gen(0.1, 3.0)
        self.length = gen(0.1, 10.0)

        self.volume = self.height * self.width * self.length
        self.mass = self.volume * gen(1.0, 4.0)


class Carriage:
    def __init__(self):
        self.height = gen(2.0, 3.0)
        self.width = gen(2.0, 3.0)
        self.length = gen(10.0, 20.0)

        self.volume = self.height * self.width * self.length
        self.carrying = self.volume * 750
        self.storage = []

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
