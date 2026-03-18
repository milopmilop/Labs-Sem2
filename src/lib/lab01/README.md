# Лабораторная работа №1

## Реализация класса Product в [model.py]:
```python
class Apartment:
    # атрибут класса (общий для всех квартир)
    currency = "RUB"

    def __init__(self, address: str, area: float, price: float, rooms: int):
        self._validate_address(address)
        self._validate_area(area)
        self._validate_price(price)
        self._validate_rooms(rooms)

        self._address = address.strip()
        self._area = float(area)
        self._price = float(price)
        self._rooms = rooms

    
    def _validate_address(self, address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Адрес не может быть пустой строкой")

    def _validate_area(self, area):
        if not isinstance(area, (int, float)):
            raise TypeError("значение должно соответствовать типа данных float")
        if area <= 0 or area > 1000:
            raise ValueError("Значение должно юыть в диапозоне (0, 1000]")

    def _validate_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("значение должно соответствовать типа данных float")
        if price < 0:
            raise ValueError("Цена должна быть >= 0")

    def _validate_rooms(self, rooms):
        if not isinstance(rooms, int):
            raise TypeError("Неверный тип данных")
        if rooms <= 0 or rooms > 20:
            raise ValueError("Количество комнат должно быть в диапозоне [1, 20]")


    @property
    def address(self) -> str:
        return self._address

    @property
    def area(self) -> float:
        return self._area

    @property
    def rooms(self) -> int:
        return self._rooms


    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        self._validate_price(value)
        self._price = float(value)


    def __str__(self) -> str:
        
        return (
            f"Apartment: {self._address} | {self._area:.1f} m² | "
            f"{self._rooms} rooms | {self._price:,.2f} {self.currency}"
        )

    def __repr__(self) -> str:
        # техническое представление, удобное для отладки
        return (
            f"Apartment(address={self._address!r}, area={self._area!r}, "
            f"price={self._price!r}, rooms={self._rooms!r})"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Apartment):
            return NotImplemented
        return (self._address, self._area, self._rooms) == (other._address, other._area, other._rooms)

    # мистербизнес метод 
    def price_per_sqm(self) -> float:
        return self._price / self._area

    def apply_discount(self, percent: float) -> float:
        # второй бизнес-метод: применить скидку в процентах
        if not isinstance(percent, (int, float)):
            raise TypeError("percent must be int or float")
        if percent < 0 or percent > 100:
            raise ValueError("percent must be in range [0, 100]")

        self._price = self._price * (1 - percent / 100)
        return self._price
```


## Файл [demo.py] проверяет функционал класса
```python
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
```