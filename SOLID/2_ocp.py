"""
Open-Closed Principle

Программные сущности (классы, модули, функции) должны быть открыты для расширения, но не для модификации.
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass


animals = [
    Animal('lion'),
    Animal('mouse')
]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')


animal_sound(animals)

"""
Самая главная проблема такой архитектуры заключается в том, что функция определяет то, какой звук издаёт то или иное
животное, анализируя конкретные объекты. Функция animal_sound не соответствует принципу открытости-закрытости,
так как, например, при появлении новых видов животных, нам, для того, чтобы с её помощью можно было бы узнавать звуки,
издаваемые ими, придётся её изменить.
"""

animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]


def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')

animal_sound(animals)

"""
Привести функцию animal_sound в соответствие с принципом открытости-закрытости можно, например, так:
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


animals = [
    Lion('lion'),
    Mouse('mouse'),
    Snake('snake')
]


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)
