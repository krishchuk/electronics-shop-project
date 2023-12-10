"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    ex1 = Item("Яблоко", 5, 100)
    assert ex1.price * ex1.quantity == 500


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
