import sys
import string
sys.stdin = open('D:/code/ALgo_math/Night at the Museum/INP.txt', 'r')
s = input()
pnt = 'a'
cnt = 0
for c in s:
    dist = abs(ord(pnt) - ord(c))
    if (dist < 13):
        cnt += dist
    else:
        cnt += (26-dist)
    pnt = c
print(cnt)