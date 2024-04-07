from product import ZeroRemainingQuantityException
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

    def avg_amount(self):
        """Метод для расчета средней стоимости товара"""
        try:
            sum_amount, sum_quantity = 0, 0
            for _ in self.goods:
                sum_amount = (_ + sum_amount)
                sum_quantity += len(_)
            return round(sum_amount / sum_quantity, 2)
        except ZeroDivisionError:
            return 0

    def add_product(self, goods_obj):
        if not goods_obj.remaining_quantity:
            raise ZeroRemainingQuantityException
        self.__goods += [goods_obj]

