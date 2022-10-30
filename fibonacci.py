def fibonacci_nth_term(index: int) -> int:
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci_nth_term(index - 1) + fibonacci_nth_term(index - 2)


def fibonacci_nth_term_even(index: int) -> int:
    if index == 0:
        return 0
    elif index == 1:
        return 2
    else:
        return 4 * fibonacci_nth_term_even(index - 1) + fibonacci_nth_term_even(index - 2)


def fibonacci_sum_upto_even(upto: int) -> int:
    current_index = 1
    current_term = 2
    current_sum = 0
    while current_term <= upto:
        current_sum += current_term
        current_index += 1
        current_term = fibonacci_nth_term_even(current_index)
    return current_sum
