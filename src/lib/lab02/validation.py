from src.lib.lab01.model import Apartment

def validate_unique_id(value: int):

    if not isinstance(value, int):
        raise TypeError(f"Value: {value} must be type: int")
    
    if value < 0:
        raise ValueError(f"Value: {value} must be > 0")
    
def validate_class_apartment(object: Apartment):

    if not isinstance(object, Apartment):
        raise TypeError(f"Object:{object} must be type: Apartment")
    
def validate_apartment_address(value: str):

    if not isinstance(value, str):
        raise TypeError(f"Value:{value} must be type: str")
    
    if value.strip() == '':
        raise ValueError(f"Value:{value} != '' ")