class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self,name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))

data = Position('Сергей', 'Иванов', 'ТОП менеджер', 100000, 25000)
data.get_full_name()
data.get_total_income()
