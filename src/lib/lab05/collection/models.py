from .base import Apartment

from .validation.validate_lab_03 import (
    validate_ceiling_height,
    validate_floor,
    validate_rooms,
    validate_terrace,
    validate_price_per_sqm
)

class Penthouse(Apartment):
    
    def __init__(self, address: str, area: float, price: float, rooms: int, is_available: bool, floor: int, terrace: bool, ceiling_height: float):
        super().__init__(address, area, price, rooms, is_available)

        if validate_floor(floor):
            self._floor = floor
        if validate_terrace(terrace):
            self._terrace = terrace
        if validate_ceiling_height(ceiling_height):
            self._ceiling_height = ceiling_height
    
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
    
    def get_info(self) -> str:
        return super().__str__()
    
    def get_address(self) -> str:
        return self._address
    
    def terrace_access_switch(self) -> bool:

        self._terrace = not self._terrace
        return self._terrace
    
    def calculate_price(self, price_per_sqm: int | float) -> float:

        validate_price_per_sqm(price_per_sqm)
        return self._area * price_per_sqm * 1.5
    

class Studio(Apartment):
    
    def __init__(self, address: str, area: float, price: float, rooms: int, is_available: bool, floor: int):
        super().__init__(address, area, price, rooms, is_available)
        
        if validate_floor(floor):
            self._floor = floor

        if validate_rooms(rooms):
            self._rooms = rooms
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

    def get_info(self) -> str:
        return super().__str__()

    def get_address(self) -> str:
        return self._address
        
    def switch_floor(self) -> int:

        self._floor = 2 if self._floor == 1 else 1
        return self._floor
    
    def calculate_price(self, price_per_sqm: int | float) -> float:
        
        validate_price_per_sqm(price_per_sqm)
        return self._area * price_per_sqm * 0.75
