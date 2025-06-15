from utils.value_cheker import ValueChecker


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