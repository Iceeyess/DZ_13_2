class Category:
    """Класс для характеристики и действий над категориями товаров"""
    total_category_count = 0
    total_unique_product = 0

    def __init__(self, name: str, description: str, goods: list) -> None:
        self.name = name
        self.description = description
        self.__goods = goods
        Category.total_category_count += 1
        Category.total_unique_product += len(goods)

    @property
    def goods(self) -> str:
        result = ''
        for product in self.__goods:
            result += f"{product.name}, {product.price} руб. Остаток: {product.remaining_quantity} шт.\n"
        return result
