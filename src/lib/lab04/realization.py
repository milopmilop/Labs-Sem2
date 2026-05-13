from dataclasses import dataclass, field
from .interfaces import ApartmentInterface

from .validate import *

@dataclass
class Apartment(ApartmentInterface):

    _address: str
    _area: float
    _price: float
    _rooms: int
    _is_available: bool

    @property
    def address(self) -> str:
        return self._address

    @property
    def area(self) -> float:
        return self._area
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def rooms(self) -> int:
        return self._rooms
    
    @property
    def is_available(self) -> bool:
        return self._is_available
    
    @rooms.setter
    def rooms(self, value: int):
        if validate_rooms(value):
            self._rooms = value
    
    @is_available.setter
    def is_available(self, value: bool) -> None:
        if validate_available(value):
            self._is_available = value
    
    @price.setter
    def price(self, value: float) -> None:
        validate_price(value)
        self._price = value
    
    def __post_init__(self):

        validate_address(self._address)
        validate_area(self._area)
        validate_price(self._price)
        validate_rooms(self._rooms)
        validate_available(self._is_available)

    def price_per_sqm(self) -> float:
        return self._price / self._area
    
    def apply_discount(self, percent: int | float) -> float:
        
        validate_percent(percent)
        self._price = self._price * (1 - percent / 100)
        return self._price

@dataclass
class Penthouse(ApartmentInterface):
    
    _address: str
    _area: float
    _price: float
    _rooms: int
    _is_available: bool
    _has_pool: bool
    
    @property
    def address(self) -> str:
        return self._address
    
    @property
    def area(self) -> float:
        return self._area
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def rooms(self) -> int:
        return self._rooms
    
    @property
    def is_available(self) -> bool:
        return self._is_available
    
    @property
    def has_pool(self) -> bool:
        return self._has_pool
    @rooms.setter
    def rooms(self, value: int):
        if validate_rooms(value):
            self._rooms = value
    
    @is_available.setter
    def is_available(self, value: bool):
        if validate_available(value):
            self._is_available = value
    
    @has_pool.setter
    def has_pool(self, value: bool):
        if validate_has_pool(value):
            self._has_pool = value

    @price.setter
    def price(self, value: int | float) -> None:
        validate_price(value)
        self._price = value
    
    def __iter__(self):
        return iter(self._apartments)
    
    def __post_init__(self):
        validate_address(self._address)
        validate_area(self._area)
        validate_price(self._price)
        validate_rooms(self._rooms)
        validate_available(self._is_available)
    
    def price_per_sqm(self) -> float:
        return (self._price / self._area) * 1.5 # - Добавился коэффициент для пентхауса.
    
    def apply_discount(self, percent_for_penthouse: int | float) -> float:
        validate_percent_for_penthouse(percent_for_penthouse) # - Добавилась своя валидация для пентхауса (Скидка не более 15 процентов).
        self._price = self._price * (1 - percent_for_penthouse / 100)
        return self._price

    def swim_into(self) -> None:
        if not self._has_pool:
            raise ValueError("Пентхаус не имеет бассейна")
        print("Плавание в бассейне пентхауса")

@dataclass
class House(HouseInterface):
    
    _apartments: list = field(default_factory=list)

    @property
    def apartments(self) -> list:
        return self._apartments
    
    def add(self, apartment: ApartmentInterface) -> None:

        validate_apartmentinterface(apartment)

        if apartment in self._apartments:
            raise ValueError

        self._apartments.append(apartment)
    
    def remove(self, apartment: ApartmentInterface) -> None:
        validate_apartmentinterface(apartment)

        if apartment not in self._apartments:
            raise ValueError

        self._apartments.remove(apartment)
    
    def get_all(self) -> list | None:
        return self._apartments.copy()
    
    def get_expensive(self) -> list:
        if self._apartments:
            return [apartment for apartment in self._apartments if apartment.price >= sum(apartment.price for apartment in self._apartments) / len(self._apartments)]
        return []
    
    def get_available(self) -> list:
        if self._apartments:
            return [apartment for apartment in self._apartments if apartment.is_available]
        return []
    
    def filter_by_interface(self) -> list:

        return [apartment for apartment in self._apartments if isinstance(apartment, ApartmentInterface)]
    
def apply_discount_for_all(house: HouseInterface, percent: int | float) -> bool:

    validate_houseinterface(house)
    validate_percent(percent)

    if house:
        print("------------")
        for obj in house.apartments:
            previous = obj.price
            obj.apply_discount(percent)
            print(f"Объект: {obj._address} -> Цена до скидки: {previous}, цена после скидки: {obj.price}")
        return "------------"
    return False

        







