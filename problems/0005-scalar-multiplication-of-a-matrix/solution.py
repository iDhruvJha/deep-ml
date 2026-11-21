import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    temp = np.array(matrix) 
    temp = temp*scalar
    return temp.tolist()