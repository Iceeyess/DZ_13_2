import pytest
from ..entities.category import Category
from ..entities.product import Product

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
                    [Product.add_product(*[value for value in a.values()], []) for a in dictionary['products']])


@pytest.fixture
def data_category_2():
    dictionary = {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 23000.00,
        "quantity": 5
      },{
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 12000.0,
        "quantity": 3
      }]}

    return Category(dictionary['name'], dictionary['description'],
                    [Product.add_product(*[value for value in a.values()], []) for a in dictionary['products']])


def test_product(data_category_1):
    assert isinstance(data_category_1.goods, list)
    for x in data_category_1.goods:
        assert x.price == 123000
        assert len(x) == 7
        assert x.__str__() == '55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_product_2():
    dictionary = {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 23000.00,
        "quantity": 5
      }, {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 33000.0,
        "quantity": 3
      }]}

    cat_class = []
    for params in dictionary['products']:
        if not cat_class:
            cat_class.append(Product.add_product(params['name'], params['description'], params['price'], params['quantity'], cat_class))
        else:
            cat_class.append(Product.add_product(params['name'], params['description'], params['price'], params['quantity'], cat_class))

    prod_class_1 = dictionary['products'][0]
    prod_class_2 = dictionary['products'][1]
    p_1 = Product(prod_class_1['name'], prod_class_1['description'], prod_class_1['price'], prod_class_1['quantity'])
    p_2 = Product(prod_class_2['name'], prod_class_2['description'], prod_class_2['price'], prod_class_2['quantity'])
    p_3 = p_1 + p_2 # __add__ method testing
    assert p_3 == 214000

