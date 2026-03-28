def solve():
    with open('05.txt', 'r') as file:
        r = False
        ranges = []
        ans = 0
        for line in file:
            if r:
                id = int(line.strip())
                for i in ranges:
                    if id >= i[0] and id <= i[1]:
                        ans += 1
                        break
            else:
                if len(line.strip())==0:
                    r = True
                    continue
                ranges.append([int(x) for x in line.strip().split('-')])

        print(ans)

solve()