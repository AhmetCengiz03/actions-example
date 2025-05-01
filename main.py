"""Example code."""

from random import randint


def estimate_frog_count():
    """Estimates random frog count"""
    return randint(1, 10)


if __name__ == "__main__":
    print(estimate_frog_count())
