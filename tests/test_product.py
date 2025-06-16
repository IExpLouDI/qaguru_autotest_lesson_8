import pytest


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