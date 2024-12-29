import pytest
from src.strings import *


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("bcdfg") == 0
    assert count_vowels("AEIOU") == 5


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("single") == "single"


def test_compress_string():
    assert compress_string("aaabb") == "a3b2"
    assert compress_string("abc") == "a1b1c1"
    assert compress_string("") == ""


def test_are_anagrams():
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("hello", "world") is False
    assert are_anagrams("Dormitory", "Dirty room") is True


# Run Tests
if __name__ == "__main__":
    test_is_palindrome()
    test_count_vowels()
    test_reverse_words()
    test_compress_string()
    test_are_anagrams()
    print("All tests passed!")
