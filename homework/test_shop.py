"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


def gen_ids(fixture_value):
    return f"Test - {fixture_value}"


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart(product):
    return Cart()


@pytest.fixture(scope="function", params=["valid_quantity",
                                          "zero_quantity",
                                          "negative_quantity",
                                          "over_maximize"
                                          ], ids=gen_ids)
def cases_for_check_quantity(request, product):
    case_type = request.param
    if case_type == "valid_quantity":
        return [product.quantity, True]
    elif case_type == "zero_quantity":
        return [0, True]
    elif case_type == "negative_quantity":
        return [-1, False]
    else:
        return [product.quantity + 1, False]


@pytest.fixture(params=["max_value", "min_value", "zero_value"], ids=gen_ids)
def cases_for_product_buy(product, request):
    case = request.param
    if case == "max_value":
        return [product.quantity, product.quantity - product.quantity]
    elif case == "min_value":
        if 0 <= product.quantity <= 1:
            return [product.quantity, 0]
        else:
            return [1, product.quantity - 1]
    else:
        return [0, product.quantity]


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """


    def test_product_check_quantity(self, product, cases_for_check_quantity):
        # TODO напишите проверки на метод check_quantity
        case_params = cases_for_check_quantity
        assert product.check_quantity(case_params[0]) == case_params[1]


    def test_product_buy(self, product, cases_for_product_buy):
        # TODO напишите проверки на метод buy
        product_counts = product.quantity
        product.buy(product_counts)
        assert product.quantity == (product_counts - product_counts)


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        other_max_value = product.quantity + 1
        with pytest.raises(ValueError) as exc:
            product.buy(other_max_value)
        assert exc.typename == 'ValueError'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_all(self, cart, product):
        print(1)
