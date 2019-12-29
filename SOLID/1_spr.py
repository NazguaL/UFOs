"""
Single Responsibility Principle

Класс должен быть ответственен лишь за что-то одно. Если класс отвечает за решение нескольких задач, его подсистемы,
реализующие решение этих задач, оказываются связанными друг с другом. Изменения в одной такой подсистеме ведут к
изменениям в другой.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self):
        pass

"""
В соответствии с принципом единственной ответственности класс должен решать лишь какую-то одну задачу.
Он же решает две, занимаясь работой с хранилищем данных в методе save и манипулируя свойствами объекта в конструкторе.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:  # PEP 3107 -- Function Annotations
        pass

    def save(self, animal: Animal):
        pass

"""
Решение проблемы с наличем двух классов Animal и AnimalDB:
Использование паттерна Фасад
"""


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return self.name

    def get(self, id):
        return self.db.get_animal(id)

    def save(self):
        self.db.save(animal=self)

"""
https://medium.com/webbdev/solid-4ffc018077da
https://medium.com/@dorela/s-o-l-i-d-principles-explained-in-python-with-examples-3332520b90ff
https://github.com/heykarimoff/solid.python
"""