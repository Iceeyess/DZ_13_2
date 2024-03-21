import pytest
from ..entities.category import Category
from ..entities.product import Product
from ..entities.instance_iteration import InstanceIterator

@pytest.fixture
def data_category_1():
    dictionary = {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }]
    }
    return Category(dictionary['name'], dictionary['description'],
                    [Product.add_product(a['name'], a['description'], a['price'], a['quantity'], []) for a in dictionary['products']])


def test_instance_iteration(data_category_1):
    to_check = InstanceIterator(data_category_1)
    for check in to_check:
        assert check.__str__() == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'