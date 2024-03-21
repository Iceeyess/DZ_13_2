import pytest, os
from ..entities.funcs import get_json_file

path_ = os.path.join('DZ_13_2', 'source', 'products.json')


def test_get_json_file():
    data = get_json_file(path_)
    result = [{'name': 'Смартфоны', 'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 23000.0, 'quantity': 5}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210400.0, 'quantity': 3}, {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 12000.0, 'quantity': 3}, {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 42000, 'quantity': 4}, {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 35000.0, 'quantity': 5}, {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 44000.0, 'quantity': 6}, {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]}, {'name': 'Телевизоры', 'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', 'products': [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}]
    assert data == result