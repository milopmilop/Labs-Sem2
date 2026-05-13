def validate_floor(floor: int) -> bool:
    if not isinstance(floor, int):
        raise ValueError("Этаж должен быть целым числом в диапазоне [0, 5]")
    return True

def validate_terrace(terrace: bool) -> bool:
    if not isinstance(terrace, bool):
        raise TypeError("Поле терраса должно быть логического типа (True/False)")
    return True

def validate_ceiling_height(ceiling_height: float) -> bool:
    if not isinstance(ceiling_height, (int, float)) or ceiling_height <= 0:
        raise ValueError("Высота потолков должна быть положительным числом")
    return True

def validate_rooms(rooms: int) -> bool:
    if not isinstance(rooms, int) or not (1 <= rooms <= 20):
        raise ValueError("Количество комнат должно быть от 1 до 20")
    return True

def validate_address(address: str) -> bool:
    if not isinstance(address, str) or not address.strip():
        raise ValueError("Адрес не может быть пустой строкой")
    return True

def validate_area(area: float) -> bool:
    if not isinstance(area, (int, float)) or not (1 <= area <= 1000):
        raise ValueError("Площадь должна быть в диапазоне [1, 1000]")
    return True

def validate_price(price: float) -> bool:
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Цена должна быть >= 0")
    return True

def validate_available(value: bool) -> bool:

    if not isinstance(value, bool):
        raise TypeError("Статус доступности должен быть True/False")
    return True

def validate_price_per_sqm(price_per_sqm: int | float) -> bool:
    
    if not isinstance(price_per_sqm, (int, float)) or price_per_sqm < 0:
        raise ValueError("Цена за квадратный метр должна быть >= 0")
    return True