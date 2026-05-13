from .strategies import *
from .collection.collection import *
# Импортируем модели для создания данных
from .collection.models import Studio, Penthouse
from .collection.base import Apartment

def get_test_data():
    """Вспомогательная функция для получения тестового набора данных."""
    return [
        # Параметры соответствуют __init__ из lab05/collection/models.py
        Apartment("ул. Ленина, 1", 50.0, 3000000.0, 2, True),
        Apartment("ул. Мира, 5", 40.0, 2500000.0, 1, False),
        Apartment("ул. Гагарина, 10", 70.0, 5000000.0, 3, True),
        # Penthouse: floor=3, terrace=True, ceiling_height=3.0
        Penthouse("пр. Центр, 1", 150.0, 20000000.0, 5, True, 3, True, 3.0),
        # Studio: floor=2
        Studio("ЖК Скай, 2", 30.0, 1500000.0, 1, True, 2)
    ]

def for_three():
    print("\n" + "="*50)
    print("GRADE 3: ФУНКЦИИ ВЫСШЕГО ПОРЯДКА (SORTED, FILTER)")
    print("="*50)
    data = get_test_data()
    
    # 1. Сортировка через встроенную функцию sorted() и передачу функций-стратегий
    print("Сортировка по цене (через функцию by_price):")
    for a in sorted(data, key=by_price):
        print(f"   {a.address}: {a.price:,.0f} руб.")
        
    # 2. Фильтрация через встроенную функцию filter()
    print("\nФильтрация: Только доступные (через функцию is_available):")
    for a in filter(is_available, data):
        print(f"   [OK] {a.address}")

def for_four():
    print("\n" + "="*50)
    print("GRADE 4: MAP, LAMBDAS И ФАБРИКИ ФУНКЦИЙ")
    print("="*50)
    data = get_test_data()
    
    # 1. Использование map и lambda для получения списка адресов в верхнем регистре
    upper_addresses = list(map(lambda x: x.address.upper(), data))
    print(f"Адреса (map + lambda): {upper_addresses}")
    
    # 2. Использование фабрики функций для создания динамического фильтра по цене
    price_filter = make_price_filter(5_000_000)
    print("\nОбъекты до 5 млн (через фабрику make_price_filter):")
    for a in filter(price_filter, data):
        print(f"   - {a.address}: {a.price:,.0f} руб.")

def for_five():
    print("\n" + "="*50)
    print("GRADE 5: ЦЕПОЧКИ (CHAINING) И CALLABLE ОБЪЕКТЫ")
    print("="*50)
    
    # Инициализация коллекции
    house = House(get_test_data())
    
    print("Выполнение цепочки операций (Method Chaining):")
    print("filter_by(Доступные) -> sort_by(Цена) -> apply(Скидка 10%)\n")
    
    # Демонстрация Fluent Interface (Grade 5)
    # Используем Callable-объекты из strategies.py
    result = (house
              .filter_by(FilterAvailable()) # Предикат-объект
              .sort_by(SortByPrice())       # Ключ-объект
              .apply(apply_discount(10)))   # Массовое изменение
              
    for a in result.get_all():
        print(f"   Результат: {a.address} | Новая цена: {a.price:,.0f} руб.")

if __name__ == "__main__":
    for_three()
    for_four()
    for_five()