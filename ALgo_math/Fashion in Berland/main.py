#import sys
#sys.stdin = open('D:/code/ALgo_math/Fashion in Berland/inp.txt', 'r')
def checkJacket(v, n):
    if n == 1:
        if v[0] == 1:
            return True
        return False
    cnt = 0
    for i in range (n):
        if v[i] == 0:
            cnt+=1
    if cnt == 1:
        return True
    return False
n = int(input())
#print(n)
v = list(map(int, input().split()))
if (checkJacket(v,n)):
    print("YES")
else: 
    print("NO")
