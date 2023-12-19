import pytest

from src.phone import Phone


def test___repr__():
    phone1 = Phone("iPhone", 100000, 30, 2)
    phone2 = Phone("Nokia", 2000, 20, 1)
    assert repr(phone1) == "Phone('iPhone', 100000, 30, 2)"
    assert repr(phone2) == "Phone('Nokia', 2000, 20, 1)"


def test_number_of_sim():
    phone3 = Phone("Samsung", 50000, 10, 2)
    assert phone3.number_of_sim == 2
    phone3.number_of_sim = 1
    assert phone3.number_of_sim == 1
    phone3.number_of_sim = 3
    assert phone3.number_of_sim == 3


def test_number_of_sim_error_zero():
    phone1 = Phone("Samsung", 10000, 20, 2)
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone1.number_of_sim = 0


def test_number_of_sim_error_float():
    phone1 = Phone("Samsung", 10000, 20, 2)
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone1.number_of_sim = 1.5
