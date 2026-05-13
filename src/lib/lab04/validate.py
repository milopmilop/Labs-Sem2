from .interfaces import ApartmentInterface, HouseInterface

def validate_percent(percent: int | float) -> None:

    if not isinstance(percent, (int, float)):
        raise TypeError

    if not (0 < percent <= 100):
        raise ValueError

def validate_apartmentinterface(apartment: object) -> None:
    
    if not isinstance(apartment, ApartmentInterface):
        raise TypeError

def validate_houseinterface(house: object) -> None:
    
    if not isinstance(house, HouseInterface):
        raise TypeError

def validate_percent_for_penthouse(percent: int | float) -> None:
    
    if not isinstance(percent, (int, float)):
        raise TypeError
    
    if not (0 < percent <= 15):
        raise ValueError

def validate_interface(interface: ApartmentInterface) -> None:
    
    if not isinstance(interface, ApartmentInterface):
        raise TypeError

def validate_has_pool(value: bool) -> None:
    
    if not isinstance(value, bool):
        raise TypeError

def validate_price(value: int | float) -> None:
    
    if not isinstance(value, (int, float)):
        raise TypeError
    
    if value <= 0:
        raise ValueError

def validate_address(address: str):

    if not isinstance(address, str) or not address.strip():
        raise ValueError("Адрес не может быть пустой строкой")
    
    return True

def validate_area(area: int | float):

    if not isinstance(area, (int, float)):
        raise TypeError("значение должно соответствовать типа данных int | float")
    
    if not (0 <= area <= 1000):
        raise ValueError("Значение должно быть в диапозоне (0, 1000)")

    return True

def validate_price(price: int | float):

    if not isinstance(price, (int, float)):
        raise TypeError("Значение должно соответствовать типу данных float")
    
    if price < 0:
        raise ValueError("Цена должна быть >= 0")

    return True

def validate_rooms(rooms: int):
    
    if not isinstance(rooms, int):
        raise TypeError("Неверный тип данных")
    
    if not (0 <= rooms <= 20):
        raise ValueError("Количество комнат должно быть в диапозоне [1, 20]")
    
    return True

def validate_available(value: bool):

    if not isinstance(value, bool):
        raise TypeError
    
    return True