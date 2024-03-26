from product import Product

class Smartphone(Product):
    """Класс для определения свойств и методов смартфона"""
    def __init__(self, efficiency: int, model: str, volume_storage: int, color: str) -> None:
        super().__init__(color)
        self.efficiency = efficiency
        self.model = model
        self.volume_storage = volume_storage

