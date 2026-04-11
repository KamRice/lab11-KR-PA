# https://github.com/KamRice/lab11-KR-PA
# Partner 1: Kameron Rice
# Partner 2: Palmer Ackerbloom

import math


def square_root(a):
    try:
        assert a > 0, "Value must be Positive Number."
        return math.sqrt(a)
    except AssertionError as err:
        print(err)


def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b):
    if not isinstance(a, int):
        print(f"TypeError for input: {a}")
        return None
    if not isinstance(b, int):
        print(f"TypeError for input: {b}")
        return None

    return a + b


def subtract(a, b):
    if not isinstance(a, int):
        print(f"TypeError for input: {a}")
        return None
    if not isinstance(b, int):
        print(f"TypeError for input: {b}")
        return None

    return a - b


def mul(a, b):
    if not isinstance(a, int):
        print(f"TypeError for input: {a}")
        return None
    if not isinstance(b, int):
        print(f"TypeError for input: {b}")
        return None

    return a * b



def logarithm(a, b):
    if not isinstance(a, int):
        print(f"TypeError for input: {a}")
        return None
    if not isinstance(b, int):
        print(f"TypeError for input: {b}")
        return None

    try:

        if a <= 0 or b <= 0:
            raise ValueError("Inputs cannot be negative.")

        return 1 / math.log(a, b)

    except ValueError:
        print(f"{ValueError.__name__}: Inputs cannot be negative.")


def exp(a, b):
    if not isinstance(a, int):
        print(f"TypeError for input: {a}")
        return None
    if not isinstance(b, int):
        print(f"TypeError for input: {b}")
        return None

    return a ** b



