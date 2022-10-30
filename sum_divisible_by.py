def sum_divisible_by(mult: int, below: int) -> int:
    sequence_end = (below - 1) // mult
    return mult * (sequence_end * (sequence_end + 1) // 2)


def sum_divisible_by_2(mult_1: int, mult_2: int, below: int) -> int:
    sum_1 = sum_divisible_by(mult_1, below)
    sum_2 = sum_divisible_by(mult_2, below)
    sum_both = sum_divisible_by(mult_1 * mult_2, below)
    return sum_1 + sum_2 - sum_both
