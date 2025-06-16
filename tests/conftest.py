import random

import pytest

from models.product import Product
from models.cart import Cart


def gen_ids(fixture_value):
	return f"Test - {fixture_value}"


@pytest.fixture(scope="function")
def product():
	return Product("book", 100, "This is a book", 1000)


@pytest.fixture(scope="function")
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
		return [product.quantity, 0] if 0 <= product.quantity <= 1 else [1, product.quantity - 1]
	else:
		return [0, product.quantity]
