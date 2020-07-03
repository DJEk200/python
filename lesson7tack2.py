class Cloth:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_square_c(self):
        return self.v / 6.5 + 0.5

    def get_square_j(self):
        return self.h * 2 + 0.3

    @property
    def get_sq_full(self):
        return f'Площадь общая ткани {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}'

class Coat(Cloth):
    def __str__(self):
        self.square_c = self.v / 6.5 + 0.5
        return f'Расход ткани на пальто {self.square_c}'


class Jacket(Cloth):
    def __str__(self):
        self.square_j = self.h * 2 + 0.3
        return f'Расход ткани на костюм {self.square_j}'

coat = Coat(6, 8)
jacket = Jacket(2, 5)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)

