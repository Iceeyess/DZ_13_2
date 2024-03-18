from config.funcs import get_json_file
from config.product import Product
from config.category import Category
import os

category_instance_list = []

path_ = os.path.join('config/products.json')
json_file = get_json_file(path_)
print(json_file)
for d_dict in json_file:
    temp_dict = {}
    product_instance_list = []
    for element in d_dict:
        if element == 'products':
            for prod_key in d_dict[element]:
                product_instance_list.append(
                    Product.add_product(prod_key['name'], prod_key['description'], prod_key['price'],
                                        prod_key['quantity'], product_instance_list))
        else:
            temp_dict |= {element: d_dict[element]}
    temp_dict |= {'products': product_instance_list}
    category_instance_list.append(Category(temp_dict['name'], temp_dict['description'], temp_dict['products']))

# for verification
for d in category_instance_list:
    print(d.goods)


