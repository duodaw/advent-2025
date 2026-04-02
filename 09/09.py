def solve():
    with open('09/09.txt', 'r') as file:
        pos = []
        ans = 0
        for line in file:
            pos.append([int(x) for x in line.strip().split(',')])
        for i in range(len(pos)-1):
            for j in range(i+1, len(pos)):
                ans = max(ans, surface(pos[i], pos[j]))
        return ans
def surface(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1]) +1)

print(solve())