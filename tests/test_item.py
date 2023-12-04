"""Здесь надо написать тесты с использованием pytest для модуля item."""
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
