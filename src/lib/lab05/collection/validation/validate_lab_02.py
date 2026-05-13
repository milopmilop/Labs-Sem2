from ..base import Apartment
from ..models import Penthouse, Studio

def validate_unique_id(value: int):

    if not isinstance(value, int):
        raise TypeError(f"Value: {value} must be type: int")
    
    if value < 0:
        raise ValueError(f"Value: {value} must be > 0")
    
def validate_class_apartment(object: Apartment):

    if not isinstance(object, Apartment):
        raise TypeError(f"Object:{object} must be type: Apartment")

def validate_class_studio(object: Studio):

    if not isinstance(object, Studio):
        raise TypeError(f"Object:{object} must be type: Studio")

def validate_class_penthouse(object: Penthouse):

    if not isinstance(object, Penthouse):
        raise TypeError(f"Object:{object} must be type: Penthouse")

def validate_apartment_address(value: str):

    if not isinstance(value, str):
        raise TypeError(f"Value:{value} must be type: str")
    
    if value.strip() == '':
        raise ValueError(f"Value:{value} != '' ")