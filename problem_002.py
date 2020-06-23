# ---------------------------
# Problem 2
# Given an array of integers, return a new array such that each element at index i of the new array is the
# product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
# ---------------------------

from functools import reduce


def calculate_product(values: list):
    result = []

    for i, v in enumerate(values):
        # Get all values in the list apart from the current one:
        multiply_values = [x for i2, x in enumerate(values) if i2 != i]

        # Use reduce to multiply all values in the list with each other and append to our new list:
        result.append(reduce(lambda x, y: x * y, multiply_values))

    return result


assert calculate_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert calculate_product([3, 2, 1]) == [2, 3, 6]
assert not calculate_product([1, 2, 3, 4, 5]) == [140, 60, 40, 30, 21]