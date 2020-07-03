
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else 'Отрицательно!'

    def __str__(self):
        return self.quantity * "*"

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_row):
        make = ''
        for i in range(int(self.quantity / cells_row)):
            make += f'{"*" * cells_row} \\n'
        make += f'{"*" * (self.quantity % cells_row)}'
        return make

cell1 = Cell(11)
cell2 = Cell(5)
print(cell1)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1.make_order(7))
print(cell1 / cell2)