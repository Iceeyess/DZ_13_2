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
    def goods(self) -> list:
        return self.__goods

    def __str__(self):
        """Строковое представление"""
        return f"{self.name}, количество продуктов: {self.__len__()} шт."


    def __len__(self):
        total_count_goods = 0
        for item in self.goods:
            total_count_goods += len(item)
        return total_count_goods
