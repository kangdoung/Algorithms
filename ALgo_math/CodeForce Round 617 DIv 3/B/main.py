import sys
sys.stdin = open('D:/code/ALgo_math/CodeForce Round 617 Div 3/B/INP.txt', 'r')

def totalc(s):
    res = 0
    while s >= 10:
        res += s - (s%10)
        s = (s%10) + (s/10)
    res += s
    return int(res)

tc = int(input())
for testcase in range(tc):
    s = int(input())
    print(totalc(s))