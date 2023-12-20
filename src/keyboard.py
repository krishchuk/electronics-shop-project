from src.item import Item


class MixinLanguage:
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Меняет язык раскладки клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(MixinLanguage, Item):
    """Класс представления клавиатуры"""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
