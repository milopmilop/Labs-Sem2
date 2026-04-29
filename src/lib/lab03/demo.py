from models import Studio, Penthouse
from collection import House

def for_three():

    # Создание объектов разных типов:
    studio_example = Studio("ул. Мира, 10", 30.0, 3_000_000, 1, True, 3)
    penthouse_example = Penthouse("ЖК 'Центр'", 120.0, 20_000_000, 4, True, 25, True, 3)

    # Вывод объектов:

    print(studio_example)
    print(penthouse_example)

    # Использование методов базового и дочернего классов:

    # - Методы базового класса (get_info):

    print(studio_example.get_info())
    print(penthouse_example.get_info())

    # - Методы дочернего класса (calculate_price):

    print(studio_example.switch_floor())
    print(penthouse_example.terrace_access_switch())

def for_four():

    # TODO: Implement task 4

    # Работа с разными типами через коллекцию:

    collection_example = House() # - Создание экземпляра класса House

    # Инициализация объектов дочерних классов:

    studio_example = Studio("ул. Мира, 10", 30.0, 3_000_000, 1, True, 5)
    penthouse_example = Penthouse("ЖК 'Центр'", 120.0, 20_000_000, 4, True, 25, True, 5)
    
    # Добавление объектов в коллекцию
    collection_example.add(studio_example)
    collection_example.add(penthouse_example)

    # Работа с разными типами через коллекцию:

    for obj in collection_example.get_all():
        print(obj.__str__())

    # Вызов одного метода - разное поведение:

    for obj in collection_example:
        print(obj.calculate_price(1000))

    # Проверка типов через isintance реализована в валидации коллекции (сами методы валидации, написанные через isinstance см. в ~/lab02/validate.py)


def for_five():

    # Реализация единого списка объектов разных типов продемонстрирована в for_four().

    # Вызов одинакового метода для разных типов и получение разных результатов:

    # - Инициализация объектов разных типов:
    studio_example = Studio("ул. Мира, 10", 30.0, 3_000_000, 1, True, 5)
    penthouse_example = Penthouse("ЖК 'Центр'", 120.0, 20_000_000, 4, True, 25, True, 5)
    
    # - Вызов метода calculate_price для разных типов:
    print(f"Цена студии: {studio_example.calculate_price(1000)}")
    print(f"Цена пентхауса: {penthouse_example.calculate_price(1000)}")

    # Фильтрация по типу:

    # - Инициализация коллекции:
    collection_example = House()

    # - Добавление объектов разных типов в коллекцию:
    collection_example.add(studio_example)
    collection_example.add(penthouse_example)

    # - Фильтрация по типу:

    studios = collection_example.filter_by_type_studio()
    penthouses = collection_example.filter_by_type_penthouse()

    print(f"Студии: {len(studios)}")
    print(f"Пентхаусы: {len(penthouses)}")

    # Сценарии реальной работы:

    # - 1. Поиск объектов типа Penthouse и изменение доступа к террасе у каждого (Легенда: "Пентхаусы теперь с закрытыми террасами"):

    for penthouse in penthouses:
        penthouse.terrace_access_switch()
        print(f"Терраса пентхауса на {penthouse.get_address()} теперь закрыта")
    
    # - 2. Поиск объектов типа Studio и перемещение жильцов, находящихся на первом этаже выше (Легенда: Первый этаж всех студий затопило и жильцы не могут самостоятельно переместится выше):


    for studio in studios:
        if studio.floor == 1:
            studio.floor = 2
            print(f"Жильцы студии на {studio.get_address()} были перемещены на второй этаж")
    
    # - 3. Поиск объектов типа Penthouse и Studio в коллекции и высчитывание стоимости каждого:

    for penthouse in penthouses:
        print(f"Цена пентхауса на {penthouse.get_address()}: {penthouse.calculate_price(1000)}")
    
    for studio in studios:
        print(f"Цена студии на {studio.get_address()}: {studio.calculate_price(1000)}")

if __name__ == "__main__":
    for_three()
    for_four()
    for_five()