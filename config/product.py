class Product:
    """Класс для характеристик и действий над свойствами товаров"""
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.remaining_quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print(f"Введена некорректная цена. Проверьте цену.")
            self.__price = self.price
        else:
            self.__price = new_price if new_price > self.price else self.price

    @classmethod
    def add_product(cls, name: str, description: str, price: float, quantity: int, lst: list):
        """"""
        new_product = cls(name, description, price, quantity) # параметры
        new_list = lst # список
        if new_list:
            for prod in new_list[::-1]: # ведем поиск с конца, как только нашли - стоп итерация
                if new_product.name == prod.name:
                    new_product.remaining_quantity += prod.remaining_quantity
                    new_product.price = prod.price
                    break
        return new_product

