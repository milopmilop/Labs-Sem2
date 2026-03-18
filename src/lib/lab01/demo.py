from model import Apartment

def main():
    print("=== Создание объектов ===")
    a1 = Apartment("Moscow, Vnukovo 1", 45, 250000, 2)
    a2 = Apartment("Moscow, Vnukovo 1", 45, 500000, 2)
    a3 = Apartment("Saint Petersburg, Nevsky 10", 60, 400000, 3)

    # вывод через print -> __str__
    print(f'Адрес: {a1.address}')    
    print(f'Кол-во кв. метров: {a1.area}')
    print(f'Цена: {a1.price}')
    print(f'a1 = {a1}')
    print('---')
    print(f'Адрес: {a2.address}')    
    print(f'Кол-во кв. метров: {a2.area}')
    print(f'Цена: {a2.price}')
    print(f'a2 = {a2}')
    print('---')
    print(f'Адрес: {a3.address}')    
    print(f'Кол-во кв. метров: {a3.area}')
    print(f'Ценa: {a3.price}')
    print(f'a3 = {a3}')
    print('__repr__')
    print("repr:", repr(a1))

    print("=== Сравнение объектов ===")
    print("a1 == a2:", a1 == a2)  # должно быть True
    print("a1 == a3:", a1 == a3)  # должно быть False

    print("=== Атрибут класса ===")
    print("атрибут класса:", Apartment.currency)
    print("атрибут примера:", a1.currency)

    print("=== Бизнес-методы ===")
    print(f"цена за кв: {a1.price_per_sqm():,.2f} {Apartment.currency}/m²")

    new_price = a1.apply_discount(10)
    print(f"после 10% скидки: {new_price:,.2f} {Apartment.currency}")
    print("после скидки:", a1)

    print("=== Setter с валидацией ===")
    a1.price = 199999.99
    print("после изменения цены:", a1)

    print("=== Некорректное создание объекта ===")

    
    try:
        a1.price = -1
    except (ValueError, TypeError) as e:
        print("Setter error:", e)

    
     # Пустой адрес
    try:
        Apartment("", 45, 250000, 2)
    except (ValueError, TypeError) as e:
        print("Пустой адрес:", e)

    # Адрес из пробелов
    try:
        Apartment("   ", 45, 250000, 2)
    except (ValueError, TypeError) as e:
        print("Адрес из пробелов:", e)

    # Площадь не число
    try:
        Apartment("Moscow", "45", 250000, 2)
    except (ValueError, TypeError) as e:
        print("Площадь не число:", e)

    # Площадь <= 0
    try:
        Apartment("Moscow", 0, 250000, 2)
    except (ValueError, TypeError) as e:
        print("Площадь <= 0:", e)

    # Площадь > 1000
    try:
        Apartment("Moscow", 1200, 250000, 2)
    except (ValueError, TypeError) as e:
        print("Площадь > 1000:", e)

    # Цена не число
    try:
        Apartment("Moscow", 45, "price", 2)
    except (ValueError, TypeError) as e:
        print("Цена не число:", e)

    # Цена < 0
    try:
        Apartment("Moscow", 45, -5000, 2)
    except (ValueError, TypeError) as e:
        print("Цена < 0:", e)

    # Комнаты не int
    try:
        Apartment("Moscow", 45, 250000, 2.5)
    except (ValueError, TypeError) as e:
        print("Комнаты не int:", e)

    # Комнаты <= 0
    try:
        Apartment("Moscow", 45, 250000, 0)
    except (ValueError, TypeError) as e:
        print("Комнаты <= 0:", e)

    # Комнаты > 20
    try:
        Apartment("Moscow", 45, 250000, 25)
    except (ValueError, TypeError) as e:
        print("Комнаты > 20:", e)

    print("\n=== Проверки setter ===")

    a = Apartment("Moscow", 45, 250000, 2)

    try:
        a.price = "abc"
    except (ValueError, TypeError) as e:
        print("Setter: цена не число:", e)

    try:
        a.price = -1
    except (ValueError, TypeError) as e:
        print("Setter: цена < 0:", e)

    print("\n=== Проверки apply_discount ===")

    try:
        a.apply_discount("10")
    except (ValueError, TypeError) as e:
        print("Скидка не число:", e)

    try:
        a.apply_discount(-5)
    except (ValueError, TypeError) as e:
        print("Скидка < 0:", e)

    try:
        a.apply_discount(120)
    except (ValueError, TypeError) as e:
        print("Скидка > 100:", e)


if __name__ == "__main__":
    main()