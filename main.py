from entities.funcs import get_json_file
from entities.product import Product
from entities.category import Category
from entities.instance_iteration import InstanceIterator
import os
from entities.smartphone import Smartphone
from entities.lawn_grass import LawnGrass
from source.dictionary import prod_key_grass, prod_key_phone

path_ = os.path.join('source/products.json')
json_file = get_json_file(path_)

category_phone = ["Телефон", "Чудесный телефон"]
category_grass = ["Трава", "Не маривана, хароЩий трава"]



# Создаем категорию смартфонов для ДЗ 16_1. JSON сложный, чтобы под него корректировать условия, поэтому без него.
# Очень не люблю , когда много условий,путает очень.
lst = []
for d in prod_key_phone:
    lst.append(Smartphone.add_product(lst, d.values()))
c_1 = Category(category_phone[0], category_phone[1], lst)
c_0 = Category(category_phone[0], category_phone[1], []) # случай без списка
print('Смартфоны с двумя смартфонами', c_1.avg_amount())
# ДЗ 16_1 Задание №2
print('Смартфоны с нулевым списком', c_0.avg_amount())

# Список для травы
lst_2 = []
for d in prod_key_grass:
    lst_2.append(LawnGrass.add_product(lst_2, d.values()))
g_1 = Category(category_grass[0], category_grass[1], lst_2)
g_0 = Category(category_grass[0], category_grass[1], []) # случай без списка
print('Травка', g_1.avg_amount())
# ДЗ 16_1 Задание №2
print('Как же плохо без травы', g_0.avg_amount())




