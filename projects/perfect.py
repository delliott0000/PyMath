def perfect_number(n: int) -> bool:

    """
    Returns True if the natural number n is a perfect number, else False.

    A natural number is a perfect number if the sum of the factors of the number is equal to the number.

    Factors include 1 but exclude the number itself.
    """

    if n == 1:
        return False
    elif n <= 0 or n % 1:
        raise ValueError('{0} is not a natural number'.format(n))

    s = 1

    for i in range(2, n // 2 + 1):
        if not n % i:
            s += i

    return s == n


if __name__ == '__main__':

    # Tests
    print(perfect_number(6))         # True
    print(perfect_number(8128))      # True

    print(perfect_number(1))         # False
    print(perfect_number(999991))    # False

    # noinspection PyTypeChecker
    print(perfect_number(-1 / 12))   # Raises ValueError
