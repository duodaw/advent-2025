import math
import heapq

def solve():
    with open('08/08.txt', 'r') as file:
        TOP_NB_NODES = 1000
        N_LARGEST = 3

        coords = []
        dists = []
        for line in file:
            coords.append([int(x) for x in line.strip().split(',')])
        n = len(coords)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = math.sqrt(math.pow(coords[i][0]-coords[j][0], 2) + math.pow(coords[i][1]-coords[j][1], 2) + math.pow(coords[i][2]-coords[j][2], 2))
                dists.append([dist, i, j])
        sorted_dist = sorted(dists, key=lambda x: x[0])
        sorted_dist = sorted_dist[:TOP_NB_NODES]
        adj = [[] for _ in range(n)]
        for i in sorted_dist:
            adj[i[1]].append(i[2])
            adj[i[2]].append(i[1])
        visited = set()
        components = []
        for i in range(n):
            if i not in visited:
                comp = []
                dfs(adj, comp, i, visited)
                components.append(comp)
        print(components)
        lens = []
        for i in components:
            heapq.heappush(lens, len(i))
            if len(lens) > N_LARGEST:
                heapq.heappop(lens)
        ans = 1
        for i in range(N_LARGEST):
            a = heapq.heappop(lens)
            if a > 0:
                ans *= a
        return ans
    
def dfs(adj, comp, s, visited):
    for i in adj[s]:
        if i not in visited:
            comp.append(i)
            visited.add(i)
            dfs(adj, comp, i, visited)

print(solve())
