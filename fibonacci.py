"""
Find terms in Fibonacci sequence.
"""


def fibonacci_nth(index: int) -> int:
    """
    Find nth term in Fibonacci sequence.
    """
    if index <= 0:
        return 0
    if index == 1:
        return 1
    return fibonacci_nth(index - 1) + fibonacci_nth(index - 2)


def fibonacci_nth_even(index: int) -> int:
    """
    Find nth even term in Fibonacci sequence.
    """
    if index <= 0:
        return 0
    if index == 1:
        return 2
    return (
        4 * fibonacci_nth_even(index - 1) + fibonacci_nth_even(index - 2)
    )


def fibonacci_sum_upto_even(upto: int) -> int:
    """
    Find largest even term in Fibonacci sequence not exceeding some value.
    """
    current_index = 1
    current_term = 2
    current_sum = 0
    while current_term <= upto:
        current_sum += current_term
        current_index += 1
        current_term = fibonacci_nth_even(current_index)
    return current_sum
