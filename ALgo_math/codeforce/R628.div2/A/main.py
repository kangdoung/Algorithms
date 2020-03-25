from math import gcd as __gcd, sqrt, ceil 
def lcm(a,b):
    return (a // __gcd(a, b) * b)

Q = int(input())
for tc in range(Q):
    n = int(input())
    for i in range(1,ceil(sqrt(n))):
        x = lcm(i,n-i)
        y =  __gcd(i,n-i)
        if (x + y == n):
            print(i)
            print(n-i)
            break
    