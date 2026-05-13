from .interfaces import ApartmentInterface, HouseInterface
from .realization import Apartment, Penthouse, House, apply_discount_for_all

# Создание объектов. В dataclass они попадают в поля _address, _area и т.д. по порядку.
apt = Apartment("ул. Ленина, 1", 50.0, 1000000.0, 2, True)
pnt = Penthouse("ул. Пушкина, 2", 100.0, 5000000.0, 4, True, True)

def for_three():
    print("\n" + "="*50)
    print("GRADE 3: Интерфейсы и Полиморфизм")
    print("="*50)
    # Вызов интерфейсных методов и демонстрация разного поведения (полиморфизм)
    for obj in [apt, pnt]:
        print(f"Объект: {type(obj).__name__} по адресу {obj.address}")
        print(f"  Цена за м2: {obj.price_per_sqm():,.2f} руб. (Расчет зависит от типа)")
        
        # Демонстрация применения скидки
        old_price = obj.price
        obj.apply_discount(10)
        print(f"  Скидка 10% применена: {old_price:,.0f} -> {obj.price:,.0f}")

def for_four():
    print("\n" + "="*50)
    print("GRADE 4: Типизация и Коллекции")
    print("="*50)
    # 1. Работа с коллекцией House
    h = House()
    h.add(apt)
    h.add(pnt)
    
    # 2. Демонстрация функции, принимающей интерфейс HouseInterface
    print(f"Применяем общую скидку 5% ко всему дому: {apply_discount_for_all(h, 5)}")

    # 3. Проверка типов через isinstance (согласно ТЗ)
    print(f"apt является ApartmentInterface: {isinstance(apt, ApartmentInterface)}")
    print(f"h является HouseInterface: {isinstance(h, HouseInterface)}")

def for_five():
    print("\n" + "="*50)
    print("GRADE 5: Архитектурные сценарии")
    print("="*50)
    house = House()
    house.add(apt)
    house.add(pnt)

    # Сценарий 1: Обработка коллекции через общие методы интерфейса (без привязки к классу)
    print("Сценарий 1 (Массовый расчет стоимости кв. метра):")
    for a in house.apartments:
        print(f"  {a.address}: {a.price_per_sqm():,.2f} руб./м2")

    # Сценарий 2: Фильтрация по интерфейсу (метод из realization.py)
    print("\nСценарий 2 (Фильтрация объектов по интерфейсу):")
    filtered = house.filter_by_interface()
    print(f"  Найдено объектов ApartmentInterface: {len(filtered)}")

    # Сценарий 3: Специфическое поведение (Пентхаус)
    print("\nСценарий 3 (Бизнес-логика пентхаусов):")
    # Проверяем наличие бассейна через свойство и вызываем специфичный метод
    if pnt.has_pool:
        pnt.swim_into()

if __name__ == "__main__":
    for_three()
    for_four()
    for_five()
