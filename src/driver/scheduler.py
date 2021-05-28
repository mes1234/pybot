class Scheduler:
    points = []
    counter = -1

    def __init__(self, count: int, power: int):
        self.setup(count, power)

    def setup(self, count: int, power: int):
        if count > 0:
            self.points = self.points+[power]*count
        else:
            self.points = [power]

    def __next__(self):
        if ((self.counter > 0) and (len(self.points) == self.counter+1)):
            self.points = [0]
            self.counter = -1
        if len(self.points) > 1:
            self.counter = self.counter+1
            return self.points[self.counter]
        else:
            return self.points[0]
