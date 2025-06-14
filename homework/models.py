class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return True if (self.quantity >= quantity >= 0) else False


    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= ValueChecker.check(quantity)
            return quantity
        else:
            raise ValueError(f"Превышено максимально-возможное значение. Max - {self.quantity}, buy - {quantity}")


    def __hash__(self):
        """Необходимо для использования в качестве ключа в словарях"""
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """


    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}


    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += ValueChecker.check(buy_count)
        else:
            self.products[product] = ValueChecker.check(buy_count)


    def remove_product(self, product: Product, remove_count: int | None = None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """

        if (remove_count is None) or (self.products[product] <= remove_count):
            self.products.pop(product)
        else:
            self.products[product] -= ValueChecker.check(remove_count)


    def clear(self):
        """
        Отчистка корзины
        """
        self.products.clear()


    def get_total_price(self) -> float:
        total_price = float(0)
        for position, counts in self.products.items():
            total_price += position.price * counts
        return round(total_price, 2)


    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        # внутри класса Product в методе buy уже предусмотрена проверка на запрос превышающий количество
        # товара на складе
        for position, count in self.products.items():
            position.buy(count)


class ValueChecker:
    @classmethod
    def check(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError("Отрицательное значение параметра")
