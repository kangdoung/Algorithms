import sys
sys.stdin = open('D:/code/ALgo_math/CodeForce Round 617 Div 3/A/INP.txt', 'r')

t = int(input())
for i in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    eve = cnt = sum = 0
    for j in range(n):
        sum += v[j]
        if (v[j]%2 == 0):
            cnt=1
        else: 
            eve=1
    
    if ( sum&1 or (cnt and eve)):
        print("YES")
    else:
        print("NO")