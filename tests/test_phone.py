from src.phone import Phone


def test___repr__():
    phone1 = Phone("iPhone", 100000, 30, 2)
    phone2 = Phone("Nokia", 2000, 20, 1)
    assert repr(phone1) == "Phone('iPhone', 100000, 30, 2)"
    assert repr(phone2) == "Phone('Nokia', 2000, 20, 1)"


def test_name():
    phone3 = Phone("Samsung", 50000, 10, 2)
    assert phone3.number_of_sim == 2
    phone3.number_of_sim = 1
    assert phone3.number_of_sim == 1
    phone3.number_of_sim = 0
    assert phone3.number_of_sim == 1
    phone3.number_of_sim = -1
    assert phone3.number_of_sim == 1
