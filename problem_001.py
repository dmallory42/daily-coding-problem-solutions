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
