from .base import Apartment

from .validation.validate_lab_02 import (

    validate_class_apartment,
    validate_apartment_address,
    validate_unique_id

)

from .models import Studio, Penthouse

class House():

    def __init__(self, apartments: list = None):
        
        if apartments is not None:
            self._apartments = apartments
        else:
            self._apartments = []

    def __len__(self):
        return len(self._apartments)
    
    def __iter__(self):
        return iter(self._apartments)
    
    def __getitem__(self, index):

        return self._apartments[index]
    
    @property
    def apartments(self): 
        return self._apartments
    
    def add(self, apartment_object: Apartment | Penthouse | Studio):
        
        validate_class_apartment(apartment_object)

        if apartment_object not in self._apartments:

            self._apartments.append(apartment_object)
            return self # Возвращаем self для цепочки
        
        return self
        
    def remove(self, apartment_object: Apartment | Penthouse | Studio):

        validate_class_apartment(apartment_object)

        if apartment_object in self._apartments:

            self._apartments.remove(apartment_object)
            return self
        
        return self
    
    def get_all(self):
        return self._apartments # Теперь возвращает список (как в ТЗ 4/5)
    
    def find_by_address(self, address: str):

        validate_apartment_address(address)

        if self._apartments:

            for object in self._apartments:

                if object.address == address:
                    return f"Object found: {object}"
            
            return "Object not found"
        
        return "List is empty"
    
    def remove_by_index(self, index: int):

        validate_unique_id(index)

        if index < len(self._apartments):

            self._apartments.pop(index)
            return self
        
        return self
        
    # --- НОВЫЕ МЕТОДЫ LAB 05 (GRADE 5 + CHAINING) ---

    def sort_by(self, key_func, reverse: bool = False):
        """Универсальная сортировка через функцию-ключ. Возвращает НОВЫЙ House."""
        new_data = sorted(self._apartments, key=key_func, reverse=reverse)
        return House(new_data)

    def filter_by(self, predicate):
        """Универсальная фильтрация через предикат. Возвращает НОВЫЙ House."""
        new_data = list(filter(predicate, self._apartments))
        return House(new_data)

    def apply(self, func):
        """Применяет функцию к каждому элементу. Возвращает self."""
        for apt in self._apartments:
            func(apt)
        return self

    # --- СТАРЫЕ МЕТОДЫ (Оставлены для совместимости) ---

    def sort_by_name(self, reverse: bool):
        self._apartments.sort(key=lambda x: x._address, reverse=reverse)
        return self
    
    def sort_by_price(self, reverse: bool):
        self._apartments.sort(key=lambda x: x._price, reverse=reverse)
        return self
    
    def sort_by_squares(self, reverse: bool):
        self._apartments.sort(key=lambda x: x._area, reverse=reverse)
        return self
    
    def get_expensive(self):
        if self._apartments:
            overall_price = sum(element._price for element in self._apartments) 
            average_price = overall_price / len(self._apartments)
            self._apartments = [apartment for apartment in self._apartments if apartment._price >= average_price]
            return self
        return self

    def get_available(self):
        self._apartments = [apartment for apartment in self._apartments if apartment._is_available]
        return self

    def filter_by_type_studio(self):
        return [apartment for apartment in self._apartments if isinstance(apartment, Studio)]

    def filter_by_type_penthouse(self):
        return [apartment for apartment in self._apartments if isinstance(apartment, Penthouse)]
    
    def filter_by_type_apartment(self):
        return [apartment for apartment in self._apartments if isinstance(apartment, Apartment)]
