from dataclasses import dataclass
from .base import Apartment

from .validate import (
    validate_ceiling_height,
    validate_floor,
    validate_terrace,
    validate_price_per_sqm
)

@dataclass
class Penthouse(Apartment):
    
    _floor: int
    _terrace: bool
    _ceiling_height: float

    @property
    def floor(self) -> int:
        return self._floor
    
    @property
    def terrace(self) -> bool:
        return self._terrace
    
    @property
    def ceiling_height(self) -> float:
        return self._ceiling_height

    @floor.setter
    def floor(self, value: int):

        validate_floor(value)
        self._floor = value

    @terrace.setter
    def terrace(self, value: bool):

        validate_terrace(value)
        self._terrace = value

    @ceiling_height.setter
    def ceiling_height(self, value: float):

        validate_ceiling_height(value)
        self._ceiling_height = value
    
    def __str__(self) -> str:
        return f"Пентхаус - Количество этажей: {self.floor}, Наличие балкона: {self.terrace}, Высота потолков: {self.ceiling_height}"
    def __repr__(self):
        return f"Penthouse(floors={self.floor}, terrace={self.terrace}, ceiling_height={self.ceiling_height})"
    
    def __eq__(self, other):
        if not isinstance(other, Penthouse):
            return NotImplemented
        return (
            self.floor == other.floor and
            self.terrace == other.terrace and
            self.ceiling_height == other.ceiling_height
        )
    
    def terrace_access_switch(self) -> bool:

        self._terrace = not self._terrace
        return self._terrace
    
    def calculate_price(self, price_per_sqm: int | float) -> float:

        validate_price_per_sqm(price_per_sqm)
        return self._area * price_per_sqm * 1.5
    
@dataclass
class Studio(Apartment):
    
    _rooms: int = 1
    _floor: int
    
    def __post_init__(self):

        validate_floor(self._floor)
        validate_rooms(self._rooms)

    @property
    def rooms(self) -> int:
        return self._rooms
    
    @property
    def floor(self) -> int:
        return self._floor
    
    @rooms.setter
    def rooms(self, value: int):

        validate_rooms(value)
        self._rooms = value
    
    @floor.setter
    def floor(self, value: int):

        validate_floor(value)
        self._floor = value
    
    def __str__(self) -> str:
        return f"Студия - Количество комнат: {self._rooms}, Количество этажей: {self._floor}"
    
    def __repr__(self):
        return f"Studio(rooms={self._rooms}, floor={self._floor})"
    
    def __eq__(self, other):
        if not isinstance(other, Studio):
            return NotImplemented
        return (
            self._rooms == other._rooms and
            self._floor == other._floor
        )

    def switch_floor(self) -> int:

        self._floor = 2 if self._floor == 1 else 1
        return self._floor
    
    def calculate_price(self, price_per_sqm: int | float) -> float:
        
        validate_price_per_sqm(price_per_sqm)
        return self._area * price_per_sqm * 0.75
