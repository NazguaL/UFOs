"""
Полиморфизм в языках программирования и теории типов — способность функции обрабатывать данные разных типов.
Есть две принципиально различных формы полиморфизма: это параметрический полиморфизм и ad-hoc-полиморфизм,
причём первая является истинной формой, а вторая — мнимой
"""

"""
Ad-hoc-полиморфизм поддерживается во многих языках посредством перегрузки функций и методов:
"""
print("Ad-hoc-полиморфизм:")

# создание класса Vehicle
class Vehicle:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")


# создание класса, который наследует Vehicle
class Car(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Car")


# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Cycle")


car_a = Vehicle()
car_a.print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()

"""
Параметрический полиморфизм
В случае параметрического полиморфизма функция реализована для всех классов одинаково, и, таким образом,
реализована вообще для произвольного типа данных. Например, функция сортировки одинакова для данных любого типа,
если функция сравнения данных задана отдельно.
"""
print("Параметрический полиморфизм")


class distance:
  def __init__(self, x=5,y=5):
    self.ft=x
    self.inch=y

  def __eq__(self, other):
    if self.ft==other.ft and self.inch==other.inch:
      return "both objects are equal"
    else:
      return "both objects are not equal"

  def __lt__(self, other):
    in1=self.ft*12+self.inch
    in2=other.ft*12+other.inch
    if in1<in2:
      return "first object smaller than other"
    else:
      return "first object not smaller than other"

  def __gt__(self, other):
    in1=self.ft*12+self.inch
    in2=other.ft*12+other.inch
    if in1<in2:
      return "first object greater than other"
    else:
      return "first object not greater than other"

d1=distance(5,5)
d2=distance()
print (d1>d2)
d3=distance()
d4=distance(6,10)
print (d1<d2)
d5=distance(3,11)
d6=distance()
print(d5<d6)


