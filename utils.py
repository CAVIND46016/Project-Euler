#Common utility functions

import random
from functools import reduce


"""Number to list of digits"""
def num2List(_num):
    return list(map(int, str(_num)))

"""List to a number"""
def list2Num(_numList):
    return int(''.join(map(str, _numList)));

def factorial(_num): 
    return reduce(lambda x, y: x * y, range(1, _num + 1), 1);

"""MATRIX"""

def zerosMatrix(_row, _col):
    return [[0 for col in range(_col)] for row in range(_row)];

def disp2DMatrix(_arr2d):
    return ("\n".join(str(row) for row in _arr2d))

def randMatrix(_matDim1, _matDim2, _lRange = 1, _hRange = 9):
    randMatrix = []
    for i in range(_matDim1):
        row = []
        for j in range(_matDim2):
            row.append(random.randint(_lRange, _hRange));
        randMatrix.append(row);
        
    return randMatrix;

def matrixProd(_mat1, _mat2):
    """Columns of first matrix must be equal to rows of the second matrix"""
    assert(len(_mat1[0]) == len(_mat2))
    """Initialize the result matrix"""
    result = [[0 for col in range(len(_mat2[0]))] for row in range(len(_mat1))]

    for i in range(len(_mat1)):
        for j in range(len(_mat2[0])):
            for k in range(len(_mat2)):
                result[i][j] += _mat1[i][k] * _mat2[k][j];
                
    return result;

"""MATRIX"""

""" Generate prime numbers less than _num"""
""" Size of _num can be in range of 10**8"""
def generatePrimes(_num):
    size  = _num // 2;
    sieve = [1] * size;
    for i in range(1, int(_num**0.5)):
        if sieve[i]:
            val = 2 * i + 1;
            tmp = ((size-1) - i) // val;
            sieve[i + val::val] = [0] * tmp;
    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0];

def isPrime(_num):
    if(_num < 2):
        return False;
    if(_num == 2 or _num == 3):
        return True;
    if(_num % 2 == 0 or _num % 3 == 0):
        return False;
    
    sqrtN = int(math.sqrt(_num)) + 1;
    for i in range(6, sqrtN + 1, 6):
        if(_num % (i-1) == 0 or _num % (i+1) == 0):
            return False;
        
    return True;
