#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def getVal(s):
    for a in range(3, (s - 3) // 3):
        for b in range(a + 1, (s - 1 - a) // 2):
            c = s - a - b;
            if(c * c == a * a + b * b):
                return (a * b * c);

def main():
    print(getVal(1000));
    
if(__name__ == "__main__"):
    main();
