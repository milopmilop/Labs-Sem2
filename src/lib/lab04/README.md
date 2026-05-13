<h1>interfaces.py</h1>

> В interfaces.py реализованы интерфейсы ApartmentInterface и HouseInterface, а также Printable, который описывает общие характеристики квартир и пентхаусов, а также методы для работы с ними.


## ApartmentInterface:

### Абстрактные методы с. флагом `@property`/`@*****.setter`:

- `address` - адрес квартиры
- `area` - площадь квартиры
- `rooms` - количество комнат
- `price` - цена квартиры
- `is_available` - доступность квартиры

### Абстрактные методы без флага `@property:`

- `price_per_sqm` - цена за квадратный метр
- `apply_discount` - применение скидки

## HouseInterface:

### Абстрактные методы с. флагом `@property`:

- `apartments` - список квартир

### Абстрактные методы без флага `@property`:

- `add` - добавление квартиры.
- `remove` - удаление квартиры.
- `get_all` - получение всех квартир.
- `get_expensive` - получение самых дорогих квартир.
- `get_available` - получение доступных квартир.

<h1>realization.py</h1>

> В realization.py реализованы классы Apartment и House, которые реализуют интерфейсы ApartmentInterface и HouseInterface соответственно.

## Импорты:

### Глобальные импорты:
- `dataclasses` - Импорт dataclass и field.


### Локальные импорты:
- `interfaces` - Импорт интерфейсов (ApartmentInterface, HouseInterface).
- `validate` - Импорт валидационных функций.

## Дата-класс Apartment(ApartmentInterface):

### Атрибуты:
- `_address` - адрес квартиры.
- `_area` - площадь квартиры.
- `_rooms` - количество комнат.
- `_price` - цена квартиры.
- `_is_available` - доступность квартиры.

### Инкапсуляция:

#### Геттеры:

- `address` - адрес квартиры.
- `area` - площадь квартиры.
- `rooms` - количество комнат.
- `price` - цена квартиры.
- `is_available` - доступность квартиры.

#### Сеттеры (Проходят `validate_*****` перед присваиванием):

- `rooms` - Изменение количества комнат.
- `is_available` - Изменение доступности квартиры.

### Методы:

- `price_per_sqm` - Цена за квадратный метр.
- `apply_discount` - Применение скидки.

## Дата-класс Penthouse(ApartmentInterface):

### Атрибуты:

- `_address` - адрес пентхауса.
- `_area` - площадь пентхауса.
- `_rooms` - количество комнат.
- `_price` - цена пентхауса.
- `_is_available` - доступность пентхауса.

### Геттеры:

- `_address` - адрес пентхауса.
- `_area` - площадь пентхауса.
- `_rooms` - количество комнат.
- `_price` - цена пентхауса.
- `_is_available` - доступность пентхауса.
- `_has_pool` - наличие бассейна.

### Сеттеры (Проходят `validate_*****` перед присваиванием):

- `rooms` - Изменение количества комнат.
- `is_available` - Изменение доступности квартиры.
- `has_pool` - Изменение наличия бассейна.

### Методы:

- `price_per_sqm` - Цена за квадратный метр.
- `apply_discount` - Применение скидки.
- `swim_into` - Плавание в бассейне пентхауса.

## Дата-класс House(HouseInterface):

### Атрибуты:

- `_apartments` - список квартир в доме.

### Геттеры:

- `apartments` - список квартир в доме.

### Методы:

- `add` - Добавление квартиры в дом.
- `remove` - Удаление квартиры из дома.
- `get_all` - Получение всех квартир в доме.
- `get_expensive` - Получение самых дорогих квартир в доме.
- `get_available` - Получение доступных квартир в доме.
- `filter_by_interface` - Фильтрация квартир по интерфейсу.

## Универсальная функция apply_discount:

```
def apply_discount_for_all(house: HouseInterface, percent: int | float) -> bool:

    validate_houseinterface(house)
    validate_percent(percent)

    if house:
        print("------------")
        for obj in house.apartments:
            previous = obj.price
            obj.apply_discount(percent)
            print(f"Объект: {obj._address} -> Цена до скидки: {previous}, цена после скидки: {obj.price}")
        return "------------"
    return False
```

<h1>validate.py</h1>

> Валидация методов/атрибутов/иных значений, применяемых в realization.py

* `validate_apartmentinterface` - Валидация интерфейса ApartmentInterface
* `validate_houseinterface` - Валидация интерфейса HouseInterface
* `validate_percent` - Валидация процента скидки
* `validate_address` - Валидация адреса
* `validate_area` - Валидация площади
* `validate_price` - Валидация цены
* `validate_rooms` - Валидация количества комнат
* `validate_is_available` - Валидация доступности
* `validate_has_pool` - Валидация наличия бассейна

<h1>demo.py</h1>

## for_three():

```
def for_three():

    print("\n" + "="*50)
    print("GRADE 3: Интерфейсы и Полиморфизм")
    print("="*50)
    # Вызов интерфейсных методов и демонстрация разного поведения (полиморфизм)
    for obj in [apt, pnt]:
        print(f"Объект: {type(obj).__name__} по адресу {obj.address}")
        print(f"  Цена за м2: {obj.price_per_sqm():,.2f} руб. (Расчет зависит от типа)")
        
        # Демонстрация применения скидки
        old_price = obj.price
        obj.apply_discount(10)
        print(f"  Скидка 10% применена: {old_price:,.0f} -> {obj.price:,.0f}")
```

<p align = 'center'> ↓ </p>

```
GRADE 3: Интерфейсы и Полиморфизм
==================================================
Объект: Apartment по адресу ул. Ленина, 1
  Цена за м2: 20,000.00 руб. (Расчет зависит от типа)
  Скидка 10% применена: 1,000,000 -> 900,000
Объект: Penthouse по адресу ул. Пушкина, 2
  Цена за м2: 75,000.00 руб. (Расчет зависит от типа)
  Скидка 10% применена: 5,000,000 -> 4,500,000
```

## for_four():

```
ef for_four():
    
    print("\n" + "="*50)
    print("GRADE 4: Типизация и Коллекции")
    print("="*50)
    # 1. Работа с коллекцией House
    h = House()
    h.add(apt)
    h.add(pnt)
    
    # 2. Демонстрация функции, принимающей интерфейс HouseInterface
    print(f"Применяем общую скидку 5% ко всему дому: {apply_discount_for_all(h, 5)}")

    # 3. Проверка типов через isinstance (согласно ТЗ)
    print(f"apt является ApartmentInterface: {isinstance(apt, ApartmentInterface)}")
    print(f"h является HouseInterface: {isinstance(h, HouseInterface)}")
```

<p align = 'center'> ↓ </p>

```
GRADE 4: Типизация и Коллекции
==================================================
Применяем общую скидку 5% ко всему дому: 525000.0
apt является ApartmentInterface: True
h является HouseInterface: True
```

## for_five():

```
def for_five():
    print("\n" + "="*50)
    print("GRADE 5: Архитектурные сценарии")
    print("="*50)
    house = House()
    house.add(apt)
    house.add(pnt)

    # Сценарий 1: Обработка коллекции через общие методы интерфейса (без привязки к классу)
    print("Сценарий 1 (Массовый расчет стоимости кв. метра):")
    for a in house.apartments:
        print(f"  {a.address}: {a.price_per_sqm():,.2f} руб./м2")

    # Сценарий 2: Фильтрация по интерфейсу (метод из realization.py)
    print("\nСценарий 2 (Фильтрация объектов по интерфейсу):")
    filtered = house.filter_by_interface()
    print(f"  Найдено объектов ApartmentInterface: {len(filtered)}")

    # Сценарий 3: Специфическое поведение (Пентхаус)
    print("\nСценарий 3 (Бизнес-логика пентхаусов):")
    # Проверяем наличие бассейна через свойство и вызываем специфичный метод
    if pnt.has_pool:
        pnt.swim_into()
```

<p align = 'center'> ↓ </p>

```
GRADE 5: Архитектурные сценарии
==================================================
Сценарий 1 (Массовый расчет стоимости кв. метра):
  ул. Ленина, 1: 20,000.00 руб./м2
  ул. Пушкина, 2: 75,000.00 руб./м2

Сценарий 2 (Фильтрация объектов по интерфейсу):
  Найдено объектов ApartmentInterface: 2

Сценарий 3 (Бизнес-логика пентхаусов):
  Пентхаус ул. Пушкина, 2: Плавание в бассейне...
```