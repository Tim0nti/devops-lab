# test_main.py
# Юнит-тесты для функции is_palindrome
from main import is_palindrome

def test_palindrome_true():
    assert is_palindrome("level") is True

def test_palindrome_false():
    assert is_palindrome("hello") is False

def test_palindrome_spaces():
    assert is_palindrome("А роза упала на лапу Азора") is True
