import csv
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 10:
            self.__name = new_name
        else:
            print('Exception: Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        parents_path = Path(__file__).parent.parent
        file_path = Path(parents_path, file)
        with open(file_path) as f:
            items = csv.DictReader(f)
            cls.all = []
            for item in items:
                item_ex = Item(item['name'], item['price'], item['quantity'])

    @staticmethod
    def string_to_number(num_string):
        if not num_string.isalpha():
            return int(float(num_string))
        else:
            return "Exception: Это не число!"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return "Exception: Складываем только объекты классов!"
