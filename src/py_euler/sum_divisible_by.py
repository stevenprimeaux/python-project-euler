"""
Calculate sum of multiples.
"""


def sum_divisible_by(below: int, mult: int) -> int:
    """
    Calculate sum of integers less than below that are divisible by mult.
    """
    sequence_end = (below - 1) // mult
    return mult * (sequence_end * (sequence_end + 1) // 2)


def sum_divisible_by_2(below: int, mult_1: int, mult_2: int) -> int:
    """
    Calculate sum of integers less than below
    that are divisible by either mult_1 or mult_2.
    """
    sum_1 = sum_divisible_by(below, mult_1)
    sum_2 = sum_divisible_by(below, mult_2)
    sum_both = sum_divisible_by(below, mult_1 * mult_2)
    return sum_1 + sum_2 - sum_both
