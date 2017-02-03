#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

from functools import reduce

def factorial(n): 
    return reduce(lambda x,y:x*y,range(1,n+1),1);

def main():
    L = 100
    print ("{}".format(sum(map(int, str(factorial(L))))))
    
if(__name__ == "__main__"):
    main();
