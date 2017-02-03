import math
from utils import generatePrimes

def getVal(k):
    N = 1;
    check = True;
    limit = math.sqrt(k);
    p = generatePrimes(k);
    for i in range(len(p)):
        a = 1;
        if(check):
            if(p[i] <= limit):
                a = math.floor(math.log(k) / math.log(p[i]));
            else:
                check = False;
        N = N * p[i] ** a;
    return N;

def main():
    print(getVal(20)); 
       
if(__name__ == "__main__"):
    main();
