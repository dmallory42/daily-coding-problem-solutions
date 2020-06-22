# ---------------------------
# Problem 1
# Given a list of numbers and a number k, return whether
# any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true
# since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?
# ---------------------------

def check_sums(values: list, k: int):
    # Create a shallow copy of values:
    values_copy = [*values]

    for i in values:
        for j in values_copy:
            # We don't want to check an element against itself:
            if values.index(i) == values_copy.index(j):
                continue
            if i + j == k:
                return True

    return False


assert not check_sums([], 17)
assert check_sums([10, 15, 3, 7], 17)
assert check_sums([10, 15, 3, 7], 25)
assert not check_sums([10, 15, 3, 7], 20)
assert not check_sums([10, 15, 3, 4], 17)
