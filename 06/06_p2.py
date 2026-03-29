def solve():
    with open('06/06.txt', 'r') as file:
        ans = 0
        L = []
        for line in file:
            L.append(line)
        l = 0

        for col in range(len(L[0])):
            s = ""
            for line in range(len(L)-1):
                s += L[line][col]
            if s.strip() == '':
                continue
            if L[len(L)-1][col].strip() != '':
                last_op = L[len(L)-1][col]
                ans += l
                if last_op == '*':
                    l = 1
                else:
                    l = 0
            if last_op == '*':
                l *= int(s.strip())
            else:
                l += int(s.strip())
        ans += l
        print(ans)
solve()