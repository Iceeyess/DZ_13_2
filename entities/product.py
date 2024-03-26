class Product:
    """Класс для характеристик и действий над свойствами товаров"""
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.remaining_quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает приватный атрибут цены"""
        return self.__price

    @price.setter
    def price(self, tuple_prices: tuple) -> None:
        """Устанавливает цену по разным условиям"""
        new_price, old_price = tuple_prices
        if new_price <= 0:
            print(f"Введена некорректная цена. Проверьте цену.")
            user_answer = int(input(f"Введите цену вручную, критерий: не должно быть меньше нуля.\n"))
            if isinstance(user_answer, (int, float)) and user_answer > 0 and user_answer > old_price:
                self.__price = user_answer
                print(f"Введена новая цена вручную {self.__price}")
            elif user_answer < old_price:
                print(f'{user_answer} Цена меньше ранее заявленной. Подтвердите, что хотите\n её ввести через "y" или опровергните через "n":\n')
                user_answer_2 = input().lower()
                if user_answer_2 == 'y':
                    self.__price = user_answer
                    print(f"Введена новая цена вручную {self.__price}")
                else:
                    self.__price = old_price
                    print(f"Старая цена осталась {self.__price }")
            else:
                self.__price = new_price
                print(f"Введена новая цена автоматически {self.__price}")
        else:
            if new_price < old_price:
                user_answer = input(
                    f'{new_price} Цена меньше ранее заявленной. Подтвердите, что хотите\n её ввести через "y" или опровергните через "n":\n').lower()
                if user_answer == 'y':
                    self.__price = new_price
                    print(f"Введена новая цена вручную {self.__price}")
                else:
                    self.__price = old_price
                    print(f"Старая цена осталась {self.__price}")
            else:
                self.__price = new_price
                print(f"Введена новая цена автоматически {self.__price}")

    @classmethod
    def add_product(cls, name: str, description: str, price: float, quantity: int, lst: list):
        """Добавляет продукт в список и удаляет один элемент, если такой ранее уже был, чтобы избежать дублирования"""
        new_product = cls(name, description, price, quantity) # параметры
        new_list = lst # список
        if issubclass(new_product.__class__, Product):
            if new_list:
                for prod in new_list[::-1]: # ведем поиск с конца, как только нашли - стоп итерация
                    if new_product.name == prod.name:
                        new_product.remaining_quantity += prod.remaining_quantity
                        new_product.price = (new_product.price, prod.price)
                        new_list.remove(prod) # стираем предыдущий ЭК из-за ненадобности (дубляжа)
                        break
            return new_product

    def __str__(self) -> str:
        """Строковое отображение ЭК"""
        return f'{self.name}, {self.price} руб. Остаток: {self.remaining_quantity} шт.'

    def __len__(self) -> int:
        """Отображает оставшееся количество товара продукта"""
        return self.remaining_quantity

    def __add__(self, other):
        """Складывает два продукта и выводит общую цену за все товары в формате:
        цена продукта х количество ЭК + цена продукта х количество другого ЭК"""
        if isinstance(other, self.__class__):
            return (self.price * self.remaining_quantity) + (other.price * other.remaining_quantity)
        raise TypeError(f"Можно складывать только ЭК Product и их дочерные ЭК между собой")
