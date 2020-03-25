#import sys
#sys.stdin = open('D:/code/ALgo_math/Bear and Game/INP.txt', 'r')

def time_boring(n, T):
    ttime = 0
    for i in range(n):
        if (T[i] - ttime) > 15:
            return ttime + 15
        else:
            ttime = T[i]
    if ( ttime + 15 ) > 90:
        return 90
    return ttime + 15

n = int(input())
T = list(map(int, input().split()))
print(time_boring(n,T))
