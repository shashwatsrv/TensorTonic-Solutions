import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    X=np.array(x)
    sig=1/(1+np.exp(-X))
    return sig
    
    pass