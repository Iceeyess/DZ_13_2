from .product import Product
from .mixin import MixinRepr


class LawnGrass(Product, MixinRepr):
    """Класс для определения класса газонной стравы"""

    def __init__(self, name: str, description: str, price: (int, float), quantity: int, color: str, country_of_origin: str,
                 germination_period: int) -> None:
        super().__init__(name, description, price, quantity, color)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
