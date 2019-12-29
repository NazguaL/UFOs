"""
Interface Segregation Principle

Создавайте узкоспециализированные интерфейсы, предназначенные для конкретного клиента. Клиенты не должны зависеть от
интерфейсов, которые они не используют.
"""


class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

"""
Класс IShape описывает методы для рисования кругов (drawCircle), квадратов (drawSquare) и прямоугольников
(drawRectangle).В результате классы, реализующие этот интерфейс и представляющие отдельные геометрические фигуры, такие,
как круг (Circle), квадрат (Square) и прямоугольник (Rectangle), должны содержать реализацию всех этих методов.

Предположим, мы решим добавить в интерфейс Shape ещё один метод, drawTriangle, предназначенный для рисования
треугольников.
Это приведёт к тому, что классам, представляющим конкретные геометрические фигуры, придётся реализовывать ещё и
метод drawTriangle.

Принцип разделения интерфейса предостерегает нас от создания интерфейсов, подобных Shape из нашего примера. Клиенты
(у нас это классы Circle, Square и Rectangle) не должны реализовывать методы, которые им не нужно использовать.
"""

class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass



