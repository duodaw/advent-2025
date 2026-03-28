

def solve():
    with open('03.txt', 'r') as file:
        ans = 0
        for line in file:
            line = line.strip()
            ml = 0
            mr = 0
            for i in range(0, len(line)-1):
                if int(line[i]) > ml:
                    ml = int(line[i])
                    mr = 0
                else:
                    mr = max(mr, int(line[i]))
            mr = max(mr, int(line[len(line)-1]))
            print(str(ml) + str(mr))
            ans += int(str(ml) + str(mr))
    print(ans)


solve()