import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    op=0
    for m in range(len(x)):
        a=abs(x[m]-y[m])
        op+=a
    return op
    pass