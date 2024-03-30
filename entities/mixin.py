from abc import ABC, abstractmethod


class TemplateForProduct(ABC):
    """Шаблон для классов класса Product"""

    @abstractmethod
    def add_product(self):
        pass


class MixinRepr:
    """Дополнительный класс реализующий продукт в читабельном виде в отладке"""

    def __repr__(self):
        return f"Был создан объект класса {self.__class__.__name__} с атрибутами: {self.__dict__}"


