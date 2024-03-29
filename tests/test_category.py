import pytest
from ..entities.category import Category
from ..entities.product import Product


@pytest.fixture
def data_category():
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
                    [Product.add_product(*[value for value in a.values()], []) for a in dictionary['products']])


def test_category(data_category):
    assert data_category.name == "Телевизоры"
    assert data_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert data_category.total_category_count == 1
    assert data_category.total_unique_product == 1
    for check in data_category.goods:
        assert str(check) == '55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
