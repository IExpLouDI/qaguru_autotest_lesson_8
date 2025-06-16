from models.product import Product
from utils.value_cheker import ValueChecker


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
        self.clear()