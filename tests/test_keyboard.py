import pytest

from src.keyboard import Keyboard


def test_language():
    kb1 = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb1.language) == "EN"


def test_change_lang():
    kb2 = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb2.language) == "EN"
    kb2.change_lang()
    assert str(kb2.language) == "RU"
    kb2.change_lang()
    assert str(kb2.language) == "EN"


def test_change_lang_wrong():
    kb3 = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError, match="property 'language' of 'Keyboard' object has no setter"):
        kb3.language = "CH"
