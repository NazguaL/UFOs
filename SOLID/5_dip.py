"""
Dependency Inversion Principle

Объектом зависимости должна быть абстракция, а не что-то конкретное.
Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций.
Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
"""


class XMLHttpService:
    pass


class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service

    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.request(url, 'POST')

"""
Здесь класс Http представляет собой высокоуровневый компонент, а XMLHttpService — низкоуровневый. Такая архитектура
нарушает пункт A принципа инверсии зависимостей: «Модули верхних уровней не должны зависеть от модулей нижних уровней.
Оба типа модулей должны зависеть от абстракций».

Класс Http не должен знать о том, что именно используется для организации сетевого соединения.
Поэтому мы создадим интерфейс Connection:
"""


class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

"""
Интерфейс Connection содержит описание метода request и мы передаём классу Http аргумент типа Connection:
"""

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')

"""
Теперь, вне зависимости от того, что именно используется для организации взаимодействия с сетью, класс Http может
пользоваться тем, что ему передали, не заботясь о том, что скрывается за интерфейсом Connection.
Перепишем класс XMLHttpService таким образом, чтобы он реализовывал этот интерфейс:
"""


class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options: dict):
        self.xhr.open()
        self.xhr.send()

"""
В результате мы можем создать множество классов, реализующих интерфейс Connection и подходящих для использования в
классе Http для организации обмена данными по сети:
"""


class NodeHttpService(Connection):
    def request(self, url: str, options: dict):
        pass


class MockHttpService(Connection):
    def request(self, url: str, options: dict):
        pass
