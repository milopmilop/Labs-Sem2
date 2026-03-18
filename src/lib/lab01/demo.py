from model import Apartment


def main():
    print("=== Создание объектов ===")
    a1 = Apartment("Moscow, Vnukovo 1", 45, 250000, 2)
    a2 = Apartment("Moscow, Vnukovo 1", 45, 250000, 2)
    a3 = Apartment("Saint Petersburg, Nevsky 10", 60, 400000, 3)

    # вывод через print -> __str__
    print(a1)

    # __repr__
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

    try:
        a1.price = -1
    except (ValueError, TypeError) as e:
        print("Setter error:", e)

    print("=== Некорректное создание объекта ===")
    try:
        bad_apartment = Apartment("", -20, -5000, 0)
        print(bad_apartment)
    except (ValueError, TypeError) as e:
        print("Creation error:", e)


if __name__ == "__main__":
    main()