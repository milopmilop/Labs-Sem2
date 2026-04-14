from src.lib.lab01.model import Apartment

from .validation import (

    validate_class_apartment,
    validate_apartment_address,
    validate_unique_id

)

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
    
    def add(self, apartment_object: Apartment):
        
        validate_class_apartment(apartment_object)

        if apartment_object not in self._apartments:

            self._apartments.append(apartment_object)
            return "Successfully added"
        
        return f"Object: {apartment_object} already in the House"
        
    def remove(self, apartment_object: Apartment):

        validate_class_apartment(apartment_object)

        if apartment_object in self._apartments:

            self._apartments.remove(apartment_object)
            return "Successfully removed"
        
        return f"No apartment {apartment_object} found"
    
    def get_all(self):
        print("-----")
        if self._apartments:
            for element in self._apartments:
                print(f"{element._address}: {element._area}, {element._price}, {element._rooms}, {element._is_available}")
            return "-----"
        return "List is empty"
    
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
            return "Successfully deleted"
        
        return "The given number is out of index"
        
    def sort_by_name(self, reverse: bool):
        
        self._apartments.sort(key=lambda x: x._address, reverse=reverse)
        return self._apartments
    
    def sort_by_price(self, reverse: bool):
        
        self._apartments.sort(key=lambda x: x._price, reverse=reverse)
        return self._apartments
    
    def sort_by_squares(self, reverse: bool):
        
        self._apartments.sort(key=lambda x: x._area, reverse=reverse)
        return self._apartments
    
    def get_expensive(self):
        
        if self._apartments:
            
            overall_price = sum(element._price for element in self._apartments) 
            average_price = overall_price / len(self._apartments)
            self._apartments = [apartment for apartment in self._apartments if apartment._price >= average_price]

            return self._apartments
        
        return "List is empty"

    def get_available(self):
        
        self._apartments = [apartment for apartment in self._apartments if apartment._is_available]
        return self._apartments