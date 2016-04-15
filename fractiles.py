from collections import defaultdict
from itertools import combinations

def fractiles(k, complexity):
    """Generator for each type of fractile"""
    return ((i, artwork(i, k, complexity)) for i in range(2 ** k))

def artwork(original_sequence, k, complexity):
    if complexity == 1:
        return original_sequence

    prev_sequence = artwork(original_sequence, k, complexity - 1)
    bits_to_check = k ** complexity

    new_sequence = 0
    for digit in range(bits_to_check):
        if prev_sequence & (1 << digit): # digit is LEAD
            to_add = original_sequence << (digit * k)
            new_sequence += to_add
        # digit is GOLD, doing nothing
    return new_sequence


def tiles(k, c, s):
    for i, fractile in fractiles(k, c):
        print(fractile)


if __name__ == "__main__":
    tiles(5, 2, 5)
