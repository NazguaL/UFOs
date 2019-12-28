"""
Liskov Substitution Principle

Необходимо, чтобы подклассы могли бы служить заменой для своих суперклассов.
"""


def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))


animal_leg_count(animals)

"""
Функция нарушает принцип подстановки (и принцип открытости-закрытости). Этот код должен знать о типах всех
обрабатываемых им объектов и, в зависимости от типа, обращаться к соответствующей функции для подсчёта конечностей
конкретного животного. Как результат, при создании нового типа животного функцию придётся переписывать.

Для того чтобы эта функция не нарушала принцип подстановки, преобразуем её с использованием требований, сформулированных
Стивом Фентоном. Они заключаются в том, что методы, принимающие или возвращающие значения с типом некоего суперкласса
(Animal в нашем случае) должны также принимать и возвращать значения, типами которых являются его подклассы.
"""


class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass


def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())


animal_leg_count(animals)



