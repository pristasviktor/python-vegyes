from src.example import *


def test_find_bigger():
    assert find_bigger(5, 3) == 5
    assert find_bigger(2, 4) == 4
    assert find_bigger(3, 3) == 3
