from math import floor, sqrt


def largest_prime_factor(dividend: int) -> int:
    current_dividend = dividend

    # dividend = 1
    if current_dividend == 1:
        return 1

    # dividend is even
    if current_dividend % 2 == 0:
        current_dividend //= 2
        while current_dividend % 2 == 0:
            current_dividend //= 2
        if current_dividend == 1:
            return 2

    current_sqrt = floor(sqrt(current_dividend))
    current_largest = current_dividend
    while True:
        is_prime = True
        current_try = 3
        while current_dividend > 1 and current_try <= current_sqrt:
            if current_dividend % current_try == 0:
                current_largest = current_try
                while current_dividend % current_try == 0:
                    current_dividend //= current_try
                current_sqrt = floor(sqrt(current_dividend))
                is_prime = False
                break
            current_try += 2
        if is_prime:
            break
    if current_dividend == 1:
        return current_largest
    return current_dividend
