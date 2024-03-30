from .product import Product
from .mixin import MixinRepr


class Smartphone(Product, MixinRepr):
    """Класс для определения свойств и методов смартфона"""

    def __init__(self, name: str, description: str, price: (int, float), quantity: int, color: str, efficiency: int, model: str,
                 volume_storage: int) -> None:
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.volume_storage = volume_storage
