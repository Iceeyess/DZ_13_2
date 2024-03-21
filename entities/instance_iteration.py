from entities.category import Category


class InstanceIterator:
    """Класс итератор"""
    def __init__(self, cat) -> None:
        self.cat = cat

    def __iter__(self) -> object:
        """Возвращает итератор"""
        self.index = 0
        return self

    def __next__(self) -> None:
        """увеличивает счетчик, возвращает нужный итерируемый объект"""
        if len(self.cat.goods) > self.index:
            self.index += 1
            return self.cat.goods[self.index - 1]
        else:
            raise StopIteration

    def __repr__(self):
        """Строковое представление"""
        return f"{self.cat.goods}"
