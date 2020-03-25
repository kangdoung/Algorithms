import sys
import string
import queue
sys.stdin = open('D:/code/ALgo_math/INP.txt', 'r')

# We can solve it by BFS

MAX = 1000 + 5
vis = [False for i in range(MAX)]
gr = [ [] for i in range(MAX) ]
dis = [0]*MAX

def dfs(s):
    vis[s] = True
    st = []
    st.append(s)
    while len(st):
        u = st.pop()
        for v in range(u):
            if not vis[v]:
                vis[v] = True
                dis[v] = dis[u] + 1
                st.append(v)

N = int(input())
for i in range(N-1):
    u, v = map(int, input().split())
    gr[u].append(v)
    gr[v].append(u)
num = int(input())
ans = 0
min_dis = MAX
for i in range(num):
    x = int(input())
    if dis[x] < min_dis or (dis[x] == min_dis and x < ans):
        min_dis = dis[x]
        ans = x
print(ans)   


