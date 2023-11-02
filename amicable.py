from collections.abc import Iterator


def get_factors(n: int) -> Iterator[int]:

    """
    Yields all proper divisors of some natural number n, including 1 but excluding n.
    """

    if n <= 0 or n % 1:
        raise ValueError('{0} is not a natural number'.format(n))

    for i in range(1, n // 2 + 1):
        if not n % i:
            yield i


def amicable(a: int, b: int) -> bool:

    """
    Returns True if natural numbers a and b are amicable, else False.

    Two natural numbers are amicable if the sum of proper divisors of the first is equal to the second, and vice versa.

    In this definition, proper divisors of a natural number include 1 but not the number itself.
    """

    sum_factors_a = sum(get_factors(a))
    sum_factors_b = sum(get_factors(b))

    return sum_factors_a == b and sum_factors_b == a


if __name__ == '__main__':

    # Tests

    print(amicable(63020, 76084))  # True
    print(amicable(220, 284))      # True

    print(amicable(36, 720))       # False
    print(amicable(3, 8))          # False

    # noinspection PyTypeChecker
    print(amicable(12.5, 75))      # Raises ValueError
