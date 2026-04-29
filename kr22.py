class Product:
    _count = 0

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
        Product._count += 1  # Ошибка

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
        super().__init__(name, price)  
        self._expiry = expiry_days

    def calculate_price(self) -> float:
        return self._price * 1.10   # 10% НДС


class DigitalProduct(Product):
    def __init__(self, name, price, download_url: str):
        super().__init__(name, price)
        self._url = download_url

    def calculate_price(self) -> float:
        return self._price * 0.9  # скидка 10%


class ProductCatalog:
    def __init__(self):
        self._items = []

    def add(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Только объекты Product")
        self._items.append(product)

    def get_all(self):
        return list(self._items)
    def get_by_type(self, product_type):
        result = []
        for item in self._items:
            if isinstance(item, product_type):
                result.append(item)
        return result
def get_cheapest(self):
    if self._items:
        min_price = min(product.calculate_price() for product in self._items)
        cheapest_products = [product for product in self._items if product.calculate_price() == min_price]
        return cheapest_products
    return "List is empty"