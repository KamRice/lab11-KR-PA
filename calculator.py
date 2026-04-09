# https://github.com/KamRice/lab11-KR-PA
# Partner 1: Kameron Rice
# Partner 2: Palmer Ackerbloom

import math


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


def div(a, b):
    if not isinstance(a, int):
        print(f"TypeError for input: {a}")
        return None
    if not isinstance(b, int):
        print(f"TypeError for input: {b}")
        return None

    try:
        return a / b

    except ZeroDivisionError:
        print("Attempted to divide by 0.")


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





