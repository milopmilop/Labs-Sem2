class Product:
    _count = 0


    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
        Product._count += 1  # ошибка


    @property
    def price(self): return self._price


    @property
    def name(self): return self._name


    def calculate_price(self) -> float:
        return self._price


    def __str__(self):
        return f"{self._name}: {self.calculate_price():.2f} руб."




class FoodProduct(Product):
    def __init__(self, name, price, expiry_days: int):
        super().__init__(name, price)  # ошибка
        self._expiry = expiry_days


    # TODO: переопределите calculate_price() — добавьте НДС 10%




class DigitalProduct(Product):
    def __init__(self, name, price, download_url: str):
        super().__init__(name, price)
        self._url = download_url


    def calculate_price(self) -> float:
        return self._price * 0.9  + # скидка 10% на цифровые




class ProductCatalog:
    def __init__(self):
        self._items = []


    def add(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Только объекты Product")
        self._items.append(product)


    def get_all(self):
        return list(self._items)

    def get_cheapest(self):
        
        if self._items:
            
            overall_price = sum(element._price for element in self._items) 
            average_price = overall_price / len(self._items)
            self._apartments = [item for apartment in self._apartments if apartment._price >= average_price]

            return self._apartments
        
        return "List is empty"
    # TODO: реализуйте get_by_type(product_type)
    # TODO: реализуйте get_cheapest()
