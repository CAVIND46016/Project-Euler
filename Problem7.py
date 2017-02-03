# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

from utils import isPrime

def getVal(limit):
    count = 1;
    candidate = 1;
    
    while(count < limit):
        candidate += 2;    
        if(isPrime(candidate)):
            count += 1;
    
    return candidate;
    
def main():
    print(getVal(10001))
        
if __name__ == "__main__":
    main();
