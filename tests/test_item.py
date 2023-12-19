"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    ex1 = Item("Яблоко", 5, 100)
    assert ex1.price * ex1.quantity == 500
    assert ex1.calculate_total_price() == 500


def test_apply_discount():
    ex2 = Item("Чайник", 2000, 10)
    ex3 = Item("Утюг", 5000, 2)
    Item.pay_rate = 0.8
    ex2.apply_discount()
    Item.pay_rate = 0.5
    ex3.apply_discount()
    assert ex2.price == 1600.0
    assert ex3.price == 2500.0


def test_name():
    ex4 = Item("Утюг", 5000, 10)
    assert ex4.name == "Утюг"
    ex4.name = "Кофеварка"
    assert ex4.name == "Кофеварка"
    ex4.name = "Ультрамегалорд"
    assert ex4.name == "Кофеварка"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[1].price == '1000'
    assert Item.all[1].quantity == '3'
    assert Item.all[4].name == 'Клавиатура'
    assert Item.all[4].price == '75'
    assert Item.all[4].quantity == '5'


def test_string_to_number():
    x1 = Item.string_to_number("12345")
    assert x1 == 12345
    x2 = Item.string_to_number("20.55")
    assert x2 == 20
    x3 = Item.string_to_number("abcd")
    assert x3 == "Exception: Это не число!"


def test___repr__():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Мышь", 200, 50)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Мышь', 200, 50)"


def test___str__():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Мышь", 200, 50)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Мышь'


def test___add__():
    item1 = Item("Смартфон", 10000, 40)
    item2 = Item("Кнопочный телефон", 200, 10)
    phone1 = Phone("Samsung", 10000, 20, 2)
    assert item1 + item2 == 50
    assert item2 + phone1 == 30


def test___add___error_item():
    item1 = Item("Смартфон", 10000, 40)
    with pytest.raises(ValueError, match="Складываем только экземпляры классов Phone или Item!"):
        result = item1 + 10


def test___add___error_phone():
    phone1 = Phone("Samsung", 10000, 20, 2)
    with pytest.raises(ValueError, match="Складываем только экземпляры классов Phone или Item!"):
        result = phone1 + "100"
