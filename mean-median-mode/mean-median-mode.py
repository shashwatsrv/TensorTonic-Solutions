import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x)

    hash = {}
    s = sum(x)
    c = len(x)

    mean = s / c

    x = sorted(x)

    if c % 2 == 0:
        median = (x[c//2 - 1] + x[c//2]) / 2
    else:
        median = x[c//2]

    for i in x:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1

    mx = max(hash.values())

    mode = min(k for k, v in hash.items() if v == mx)

    return (float(mean), float(median), float(mode))