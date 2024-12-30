from src.lists import *


def test_find_maximum():
    assert find_maximum([1, 2, 3, 4, 5]) == 5
    assert find_maximum([-10, -20, -30, -5]) == -5
    assert find_maximum([42]) == 42
    assert find_maximum([]) is None  # Handle empty list


def test_separate_even_odd():
    assert separate_even_odd([1, 2, 3, 4, 5]) == ([2, 4], [1, 3, 5])
    assert separate_even_odd([10, 15, 20, 25]) == ([10, 20], [15, 25])
    assert separate_even_odd([2, 4, 6]) == ([2, 4, 6], [])
    assert separate_even_odd([1, 3, 5]) == ([], [1, 3, 5])
    assert separate_even_odd([]) == ([], [])


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list([42]) == [42]
    assert reverse_list([]) == []


def test_filter_and_square():
    assert filter_and_square([5, 12, 13]) == [144, 169]
    assert filter_and_square([9, 10, 11]) == [121]
    assert filter_and_square([3, 7]) == []
    assert filter_and_square([]) == []


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([42, 42, 42]) == [42]
    assert remove_duplicates([5, 1, 2, 1, 5, 7]) == [5, 1, 2, 7]
    assert remove_duplicates([]) == []
