"""
Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным).
Инкапсуляция делает некоторые из компонент доступными только внутри класса.
"""


class A:
    def _private(self):
        print("Это приватный метод!")

a = A()
a._private()


class B:
    def __hidden(self):
        print("Это скрытый метод!")

b = B()
# b.__hidden  # AttributeError: 'B' object has no attribute '__hidden'
"""
Но  атрибут всё равно остаётся доступным под именем _ИмяКласса__ИмяАтрибута:
"""
b._B__hidden()