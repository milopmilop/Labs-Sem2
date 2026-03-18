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