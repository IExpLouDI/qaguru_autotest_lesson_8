import random
import pytest

from tests.conftest import product


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_with_default_buy_count(self, cart, product):
        cart.add_product(product)
        for position, count in cart.products.items():
            assert product == position and cart.products[position] == 1


    def test_add_product_with_some_buy_count(self, cart, product):
        random_value = random.randint(2, 100)
        cart.add_product(product, random_value)
        for position, count in cart.products.items():
            assert product == position and cart.products[position] == random_value


    def test_add_product_exists_in_cart(self, cart, product):
        random_valuet = random.randint(2, 100)
        cart.add_product(product)
        cart.add_product(product, random_valuet)

        for position, count in cart.products.items():
            assert product == position and cart.products[position] == random_valuet + 1


    def test_remove_product_with_none(self, cart, product):
        cart.add_product(product)
        cart.remove_product(product)
        assert product not in cart.products


    def test_remove_product_with_count_more_then_exists(self, cart, product):
        cart.add_product(product, 6)
        cart.remove_product(product, 7)
        assert product not in cart.products


    def test_remove_product_with_count_less_then_exists(self, cart, product):
        cart.add_product(product, 7)
        cart.remove_product(product, 6)
        assert cart.products[product] == 1


    def test_remove_product_with_count_less_then_exists(self, cart, product):
        cart.add_product(product, 7)
        cart.remove_product(product, 6)
        assert cart.products[product] == 1


    def test_remove_product_with_remove_negative_count(self, cart, product):
        cart.add_product(product, 7)

        with pytest.raises(ValueError) as exc:
            cart.remove_product(product, -1)
        assert exc.typename == 'ValueError'


    def test_clear(self, cart, product):
        cart.add_product(product)
        product_exists_in_cart = product in cart.products
        cart.clear()
        product_in_cart_after_clear = product in cart.products
        assert product_exists_in_cart != product_in_cart_after_clear


    def test_get_total_price(self, cart, product):
        product_price = product.price
        random_quantity = random.randint(1, 100)
        result_total_price = round(float(product_price * random_quantity), 2)

        cart.add_product(product, random_quantity)

        assert result_total_price == cart.get_total_price()


    def test_buy_more_then_exists_in_product(self, cart, product):
        max_count = product.quantity
        cart.add_product(product, max_count + 1)
        with pytest.raises(ValueError) as exc:
            cart.buy()
        assert exc.typename == 'ValueError'


    def test_buy_some_product(self, cart, product):
        product_quantity = product.quantity
        add_product = random.randint(1, product.quantity)
        cart.add_product(product,add_product)
        cart.buy()
        assert (product.quantity == product_quantity - add_product) and (product not in cart.products)
