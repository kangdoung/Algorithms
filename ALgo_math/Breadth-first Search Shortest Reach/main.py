import sys
import string
import queue
sys.stdin = open('D:/code/ALgo_math/INP.txt', 'r')

MAX = 1005
visited = [0 for i in range(MAX)]
graph = [ [] for i in range (MAX) ]

def BFS(s):
    q = queue.Queue()
    visited[s] = 0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if visited[v] == 0:
                visited[v] = visited[u] + 6
                q.put(v)

Q = int(input())
 
for _ in range(Q):
    V, E = map(int, input().split())
 
    for i in range(MAX):
        graph[i].clear()
        visited[i] = 0
        #dist[i] = 0
     
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
     
    s = int(input())
    BFS(s)
 
    for i in range(1, V + 1):
        if i == s:
            continue
         
        print(visited[i] if visited[i] else -1, end=' ')
 
    print()

