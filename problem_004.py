# ---------------------------
# Problem 3
# Given an array of integers, find the first missing positive integer in
# linear time and constant space. In other words, find the lowest positive
# integer that does not exist in the array. The array can contain duplicates
# and negative numbers as well.
# ---------------------------


def find_first_missing_integer(vals: list):
    # Convert list values to absolute values
    vals = [abs(val) for val in vals]

    i = 1
    max_val = max(vals)

    while i <= (max_val + 1):
        if i not in vals:
            return i

        i += 1


assert find_first_missing_integer([3, 4, -1, 1]) == 2
assert find_first_missing_integer([1, 2, 0]) == 3
assert find_first_missing_integer([0, -4, -3, 2, 5, 5, -1, -6, 7, -8, 9, 10, -12]) == 11
assert find_first_missing_integer([0]) == 1
assert find_first_missing_integer([-1, 0]) == 2
