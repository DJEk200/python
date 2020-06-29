class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начала движение.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} {self.speed} км/ч.')


class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} {self.speed} км/ч.')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной! Сбавьте скорость'
        else:
            return f'Скорость {self.name} в пределах нормы'

class SportCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

class WorkCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} {self.speed} км/ч.')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной! Сбавьте скорость'
        else:
            return f'Скорость {self.name} в пределах нормы'

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

audi = SportCar('Audi', 'Red', 100, False)
lada = TownCar('Lada', 'White', 50, False)
zil = WorkCar('ZIL', 'Rose', 60, False)
bmw = PoliceCar('BMW', 'Blue', 110, True)
print(lada.turn('направо'))
print(f'{lada.name} покрашена в {lada.color} цвет')
print(f'{zil.go()} {zil.show_speed()}')
print(f'Машина {bmw.name} полицейская? {bmw.is_police}')
bmw.show_speed()