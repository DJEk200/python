class Road:
    def __init__(self, _length, _width, thickness):
        self._length = _length
        self._width = _width
        self.thickness = thickness
        self.weigth = 25

    def computation(self):
        return self.weigth * self._width * self.thickness * self._length / 1000

s = Road(20, 5000, 5)
print(s.computation())
