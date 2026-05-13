from abc import ABC, abstractmethod

class ApartmentInterface(ABC):

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    @property
    @abstractmethod
    def area(self) -> str:
        ...

    @property
    @abstractmethod
    def rooms(self) -> int:
        ...

    @property
    @abstractmethod
    def price(self) -> float:
        ...

    @property
    def is_available(self) -> bool:
        ...

    @is_available.setter
    @abstractmethod
    def is_available(self, value: bool) -> None:
        ...
    
    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        ...

    @abstractmethod
    def price_per_sqm(self) -> float:
        ...

    @abstractmethod
    def apply_discount(self, percent: int | float) -> float:
        ...

class Printable(ABC):

    @abstractmethod
    def to_string(self, obj: ApartmentInterface) -> str:
        ...

class HouseInterface(ABC):

    @property
    @abstractmethod
    def apartments(self) -> list:
        ...
    
    @abstractmethod
    def add(self, apartment: ApartmentInterface) -> None:
        ...
    
    @abstractmethod
    def remove(self, apartment: ApartmentInterface) -> None:
        ...

    @abstractmethod
    def get_all(self) -> list:
        ...
    
    @abstractmethod
    def get_expensive(self) -> list:
        ...
    
    @abstractmethod
    def get_available(self) -> list:
        ...