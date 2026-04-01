import math
import heapq

def solve():
    with open('08/08.txt', 'r') as file:
        TOP_NB_NODES = 1000
        coords = []
        dists = []
        for line in file:
            coords.append([int(x) for x in line.strip().split(',')])
        n = len(coords)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = euc_dist(coords[i], coords[j])
                dists.append([dist, i, j])
        sorted_dist = sorted(dists, key=lambda x: x[0])
        cnt = 0
        adj = [[] for _ in range(n)]
        for i in sorted_dist[:TOP_NB_NODES]:
            adj[i[1]].append(i[2])
            adj[i[2]].append(i[1])
            
        while True:
            lastConnection = sorted_dist[TOP_NB_NODES+cnt]
            adj[lastConnection[1]].append(lastConnection[2])
            adj[lastConnection[2]].append(lastConnection[1])
            visited = set()
            dfs(adj, 0, visited)
            if len(visited) == n:
                return coords[lastConnection[1]][0] * coords[lastConnection[2]][0]
            cnt += 1
    
def dfs(adj, s, visited):
    for i in adj[s]:
        if i not in visited:
            visited.add(i)
            dfs(adj, i, visited)

def euc_dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2) + math.pow(a[1]-b[1], 2) + math.pow(a[2]-b[2], 2))

print(solve())
