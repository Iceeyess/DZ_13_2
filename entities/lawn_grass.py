from product import Product

class LawnGrass(Product):
    """Класс для определения класса газонной стравы"""
    def __init__(self, country_of_ofigin: str, germination_period: int, color: str) -> None:
        super().__init__(color)
        self.country_of_ofigin = country_of_ofigin
        self.germination_period = germination_period

