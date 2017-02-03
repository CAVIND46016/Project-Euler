#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from functools import reduce
from utils import factorial

def curiousNumber(num):
    l = list(map(int, str(num)));
    sum = 0;
    for i in l:
        sum += factorial(i);
        
    if(num == sum):
        return True;
    else:
        return False;
    
def main():
    c = 3;
    sum = 0
    limit = 100000 # random number
    while(c < limit):
        if(curiousNumber(c)):
            sum += c;
        c += 1;
        
    print("{}".format(sum));
    
if(__name__ == "__main__"):
    main();
