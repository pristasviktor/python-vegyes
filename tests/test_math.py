from src.math import *


# Tests for generate_fibonacci
def test_generate_fibonacci():
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(0) == []
    assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Tests for is_prime
def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(1) is False


# Tests for generate_primes_below
def test_generate_primes_below():
    assert generate_primes_below(10) == [2, 3, 5, 7]
    assert generate_primes_below(2) == []
    assert generate_primes_below(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert generate_primes_below(0) == []


# Tests for factorial
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


# Tests for sum_of_digits
def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(4567) == 22
    assert sum_of_digits(1001) == 2


# Tests for find_pythagorean_triples
def test_find_pythagorean_triples():
    assert find_pythagorean_triples(20) == [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
    assert find_pythagorean_triples(10) == [(3, 4, 5), (6, 8, 10)]
    # assert find_pythagorean_triples(50) == [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), ...]  # Truncated for brevity
