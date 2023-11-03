def perfect_number(n: int) -> bool:

    """
    Returns True if the natural number n is a perfect number, else False.

    A natural number is a perfect number if the sum of the factors of the number is equal to the number.

    Factors include 1 but exclude the number itself.
    """

    s = 0

    for i in range(1, n // 2 + 1):
        if not n % i:
            s += i

    return s == n


if __name__ == '__main__':

    # Tests
    print(perfect_number(6))         # True
    print(perfect_number(28))        # True
    print(perfect_number(8128))      # True

    print(perfect_number(99999991))  # False
