from collections.abc import Iterator


Complex = int | float | complex


def fibonacci_numbers(*, first: Complex = 1, second: Complex = 2, limit: Complex = 10000) -> Iterator[Complex]:

    """
    Generates terms of a Fibonacci sequence.

    A Fibonacci sequence is a sequence of numbers such that each term is equal to the sum of the previous two terms.

    Stops generating terms when the absolute value (ABS) of the limit is exceeded by the ABS of the next term.

    The sequence usually starts with (1, 2, ...) but this can be changed by specifying the first and second values.

    Non-real numbers (a + bi : b != 0) can also be passed to generate complex Fibonacci sequences.

    Note in this case that the ABS of a + bi is defined to be equal to sqrt(a ** 2 + b ** 2).
    """

    abs_limit = abs(limit)

    for term in first, second:
        if abs(term) <= abs_limit:
            yield term
        else:
            return

    while abs(first + second) <= abs_limit:
        first, second = second, first + second
        yield second


if __name__ == '__main__':

    # Tests

    for w in fibonacci_numbers():
        ...

    for x in fibonacci_numbers(limit=10 ** 100):
        ...

    for y in fibonacci_numbers(first=2, second=4):
        ...

    for z in fibonacci_numbers(first=5-7j, second=-2-2j, limit=1000):
        ...
