"""
Find palindrome product.
"""


def reverse(to_reverse: int) -> int:
    """
    Reverse a number.
    """
    rev = 0
    while to_reverse > 0:
        rev = (10 * rev) + (to_reverse % 10)
        to_reverse //= 10
    return rev


def is_palindrome(to_check: int) -> int:
    """
    Determine if integer is palindrome.
    """
    return reverse(to_check) == to_check


def largest_palindrome_product(digits: int) -> int:
    """
    Find largest palindrome that is
    product of 2 numbers with specified number of digits.
    """
    mult_min = int("1" + ("0" * (digits - 1)))
    mult_max = int("9" * digits)
    p_largest = 0

    mult_1 = mult_max
    while mult_1 >= mult_min:
        mult_2 = mult_max
        while mult_2 >= mult_1:
            p_current = mult_1 * mult_2
            if p_current <= p_largest:
                break
            if is_palindrome(p_current):
                p_largest = p_current
            mult_2 -= 1
        mult_1 -= 1

    return p_largest
