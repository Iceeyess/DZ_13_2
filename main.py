from entities.funcs import get_json_file
from entities.product import Product
from entities.category import Category
from entities.instance_iteration import InstanceIterator
import os
from entities.smartphone import Smartphone
from entities.lawn_grass import LawnGrass

path_ = os.path.join('source/products.json')
json_file = get_json_file(path_)
product_instance_list = []
prod_key_phone = {
    "name": "Samsung Galaxy",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 23000.00,
    "quantity": 5,
    "color": "Зеленый",
    "efficiency": 48,
    "model": " C23 Ultra",
    "volume_storage": 5000
}
prod_key_grass = {"name": "Газонная трава",
                  "description": "Травосмесь \"Экологичная\" отлично обеспечит полное выздоровление почвы. Семена, находящиеся в составе, обеспечивают уничтожение эрозии. Семена газона состоят из разнообразия неприхотливых растений, а также могут применяться для корма животных.\nПакета данного набора травосмеси в 5 кг хватает для засеивания - 100 кв. м.",
                  "price": 1046.0,
                  "quantity": 5,
                  "color": "Темно-зеленый",
                  "country_of_origin": "Россия",
                  "germination_period": 40
                  }

print(repr(Smartphone.add_product([], prod_key_phone.values())))
print(repr(LawnGrass.add_product([], prod_key_grass.values())))

