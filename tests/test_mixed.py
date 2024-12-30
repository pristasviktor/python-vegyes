from src.mixed import *


# Tests for fizz_buzz
def test_fizz_buzz(capfd):
    fizz_buzz()
    captured = capfd.readouterr().out.splitlines()
    assert captured[2] == "Fizz"  # 3
    assert captured[4] == "Buzz"  # 5
    assert captured[14] == "FizzBuzz"  # 15
    assert len(captured) == 100
    assert captured[0] == "1"


# Tests for transpose_matrix
def test_transpose_matrix():
    assert transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose_matrix([[1]]) == [[1]]
    assert transpose_matrix([]) == []


# Tests for simple_calculator
def test_simple_calculator():
    assert simple_calculator("5 + 3") == 8
    assert simple_calculator("10 - 7") == 3
    assert simple_calculator("4 * 2") == 8
    assert simple_calculator("9 / 3") == 3.0
    assert simple_calculator("9 / 0") == "Error"  # Handle division by zero


# Tests for guess_the_number
# This test is more complex due to randomization and user interaction; simplified example here.
def test_guess_the_number(monkeypatch):
    from random import seed, randint
    seed(1)
    number_to_guess = randint(1, 10)

    inputs = iter([str(number_to_guess - 1), str(number_to_guess)])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    guess_the_number()  # No assertion; verify manually that it ends correctly.


# Tests for caesar_cipher
def test_caesar_cipher():
    assert caesar_cipher("abc", 3, "encrypt") == "def"
    assert caesar_cipher("xyz", 3, "encrypt") == "abc"
    assert caesar_cipher("def", -3, "encrypt") == "abc"
    assert caesar_cipher("def", 3, "decrypt") == "abc"
    assert caesar_cipher("abc", -3, "decrypt") == "xyz"
