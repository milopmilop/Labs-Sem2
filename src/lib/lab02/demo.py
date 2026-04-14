from .collection import House
from src.lib.lab01.model import Apartment

# Создание экземпляра класса House:
examplar_apartment = House()

"""
# Инициализация нескольких объектов класса House:

test_object_01 = Apartment("smth_01", 45.0, 3500000, 1, False)
test_object_02 = Apartment("smth_02", 55.0, 4500000, 2, False)

# Инициализация нескольких объектов класса House:
print(examplar_apartment.add(test_object_01))
print(examplar_apartment.add(test_object_02))

# Вывод всех объектов
print(examplar_apartment.get_all())

# Удаление одного из объектов класса House:
print(examplar_apartment.remove(test_object_01))

# Повторный вывод коллекции:
print(examplar_apartment.get_all())

print(examplar_apartment.find_by_address("smth_02"))
# Если элемент коллекции не найден: (Выведет: No object found)
print(examplar_apartment.find_by_address("the addres that's not in collection"))

# Использование dunder-метода __len__():
print(f"Длина коллекции: {len(examplar_apartment)}")

# Использование цикла for:
for object in examplar_apartment:
    print(f"Object: {object}")

# Ограничение на дубликаты:
print(examplar_apartment.add(test_object_02))

# Индексация коллекции:
print(examplar_apartment[0])

# Реализация сортировки:
"""

# Инициализация объектов класса Apartment:
test_object_03 = Apartment("Bsmth", 45.0, 340000000, 2, False)
test_object_04 = Apartment("Asmth", 55.0, 440000000, 3, True)
test_object_05 = Apartment("Dsmth", 65.0, 540000000, 4, False)
test_object_06 = Apartment("Csmth", 75.0, 640000000, 5, True)

# Инициализация доп. объектов экземпляра класса House:
examplar_apartment.add(test_object_03)
examplar_apartment.add(test_object_04)
examplar_apartment.add(test_object_05)
examplar_apartment.add(test_object_06)

"""
# ДО:
print(examplar_apartment.get_all())

# Сортировка:
print(examplar_apartment.sort_by_name())

# ПОСЛЕ:
print(examplar_apartment.get_all())

# Демонстрация фильтрации:

# Свободные квартиры:
print(examplar_apartment.get_available())

# Самые дорогие относительно средней стоимость всех квартир в доме:
print(examplar_apartment.get_expensive())
"""

"""
# Сценарии работы коллекции:

# 1. Поиск просторных и дорогих квартир (Клиент):

# 1) Поиск доступных для заселения квартир:

available_apartments = examplar_apartment.get_available()
print(available_apartments)

# 2) Поиск среди доступных для заселения квартир наиболее дорогих:

most_expensive = examplar_apartment.get_expensive()
print(most_expensive)

# 3) Поиск среди дорогих и доступных для заселения квартир самых больших по площади:

biggest_by_squares = examplar_apartment.sort_by_squares()

# 4) Вывод:

print(examplar_apartment[0])

"""

"""
# 2. Обновление статусов квартир и их цен (Квартиры подорожали, плата за ренту стала больше и ебать к сожалению никто не тянет()):

# 1) Обновление статусов квартир:

for element in examplar_apartment:
    element._is_available = True

# 2) Обновление цен на квартиры:

for element in examplar_apartment:
    element._price += element._price * 0.1

# Вывод:
print(examplar_apartment.get_all())

"""

# 3. Сортировка квартир по доступности и выбор самой дешевой из них (Клиент):

# 1) Сортировка квартир по доступности:

print(examplar_apartment.get_available())

# 2) Поиск самой дешевой:

print(examplar_apartment.sort_by_price(reverse=False))

# Вывод:

print(examplar_apartment[0])