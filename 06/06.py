def solve():
    with open('06.txt', 'r') as file:
        ops = []
        L = []
        for line in file:
            L.append(line.strip().split())
        n = len(L)
        ops = L[n-1]
        ans = 0
        for col in range(0, len(ops)):
            l = 0
            if ops[col] == '*':
                l = 1
            for line in range(0, n-1):
                if ops[col]=='*':
                    l *= int(L[line][col])
                else:
                    l += int(L[line][col])
            ans += l
        print(ans)
solve()