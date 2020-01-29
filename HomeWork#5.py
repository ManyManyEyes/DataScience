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


def load(quantity):
    carriage1 = Carriage()
    volume_left = carriage1.volume
    carrying_left = carriage1.carrying
    i = 1
    for boxes in range(quantity):
        batch = Box()
        if volume_left < batch.volume:
            print(f"The box {i} will not fit: box volume {batch.volume}, remaining volume in the carriage {volume_left}")
            break
        if carrying_left < batch.mass:
            print(f"The box {i} will not fit: box mass {batch.mass}, remaining carrying in the carriage {carrying_left}")
            break
        volume_left = volume_left-batch.volume
        carrying_left = carrying_left-batch.mass
        print(f"""The box {i} is shipped. Box parameters: 
        height: {batch.height} 
        weight: {batch.width}
        length: {batch.length} 
        volume: {batch.volume}
        mass: {batch.mass}
        Left volume in the carriage {volume_left}, left carrying in the carriage {carrying_left}""")
        i += 1

if __name__ == '__main__':
    load(10)