import math
import itertools

numbers = [1, 2, 3, 4, 5, 7]
permutations = itertools.permutations(numbers)

for (x1, x2, x3, x4, x5, x6) in permutations:
    # Verify condition on ordering
    if (x1 > x3) or (x2 > x4) or (x3 > x5) or (x4 > x6):
        pass
        #continue # ambiguity in the problem statement ?

    # Verify condition on sum
    if (x1 != x2+x3) and (x2 != x1+x3) and (x3 != x1+x2):
        continue
    if (x2 != x3+x4) and (x3 != x2+x4) and (x4 != x2+x3):
        continue
    if (x3 != x4+x5) and (x4 != x3+x4) and (x5 != x3+x4):
        continue
    if (x4 != x5+x6) and (x5 != x4+x6) and (x6 != x4+x5):
        continue

    print('Found solution:', x1, x2, x3, x4, x5, x6)