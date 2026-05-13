# strategies.py

# --- GRADE 3: Простые функции для sorted() и filter() ---

def by_price(apt):
    """Стратегия получения цены."""
    return apt.price

def by_area(apt):
    """Стратегия получения площади."""
    return apt.area

def by_address(apt):
    """Стратегия получения адреса."""
    return apt.address

def is_available(apt):
    """Предикат доступности."""
    return apt.is_available

def is_expensive(apt):
    """Предикат дороговизны (выше 4 млн)."""
    return apt.price > 4000000


# --- GRADE 4: Фабрики функций ---

def make_price_filter(max_price):
    """Создает фильтр для объектов не дороже max_price."""
    def filter_func(apt):
        return apt.price <= max_price
    return filter_func


# --- GRADE 5: Callable-объекты (Стратегии) ---

class SortByPrice:
    """Объект-стратегия для сортировки по цене."""
    def __call__(self, apt):
        return apt.price

class FilterAvailable:
    """Объект-стратегия для фильтрации доступных."""
    def __call__(self, apt):
        return apt.is_available

def apply_discount(percent):
    """Фабрика функций для массового применения скидки (метод apply)."""
    def transform(apt):
        apt.apply_discount(percent)
        return apt
    return transform
