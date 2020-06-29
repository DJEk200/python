class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки{self.title}')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У Вас в руках {self.title}. Ручка — письменная принадлежность, '
              f'с помощью которой можно оставить чернильный след на поверхности.')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У Вас в руках простой {self.title} с грифелем в деревянной оправе.')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У Вас в руках {self.title}. {self.title} инструмент для письма и рисования при помощи краски, '
              f'стекающей из резервуара к наконечнику из пористого материала.')



pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()