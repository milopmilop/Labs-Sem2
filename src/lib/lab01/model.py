
from .validate import (
    validate_address,
    validate_area,
    validate_price,
    validate_rooms,
    validate_available
)

class Apartment:

    def __init__(self, address: str, area: float, price: float, rooms: int, is_available: bool):
        
        if validate_price(price):
            self._price = price

        if validate_address(address):
            self._address = address

        if validate_area(area):
            self._area = area
        
        if validate_rooms(rooms):
            self._rooms = rooms

        if validate_available(is_available):
            self._is_available = is_available
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

    @property
    def is_available(self) -> bool:
        return self._is_available
    
    @is_available.setter
    def is_available(self, value: bool):

        if validate_available(value):
            self._is_available = value
            
    @price.setter
    def price(self, value: float):

        if validate_price(value):
            self._price = float(value)

    def __str__(self) -> str:
        
        return (
            f"Apartment: {self._address} | {self._area:.1f} m² | "
            f"{self._rooms} rooms | {self._price:,.2f}"
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

    def apply_discount(self, percent: int | float) -> float:

        # второй бизнес-метод: применить скидку в процентах
        if not isinstance(percent, (int, float)):
            raise TypeError("percent must be int or float")
        
        if not (0 < percent <= 100):
            raise ValueError("percent must be in range [0, 100]")
        
        self._price = self._price * (1 - percent / 100)
        return self._price