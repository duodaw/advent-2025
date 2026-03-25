

def solve():
    with open('03.txt', 'r') as file:
        ans = 0
        for line in file:
            line = line.strip()
            jolt = ""
            cnt = 12
            n = len(line)
            l = 0
            r = n - cnt + 1
            for i in range(12):
                fl = 0
                tmpL = 0
                for j in range(l, r):
                    if int(line[j]) > fl:
                        fl = int(line[j])
                        tmpL = j
                l = tmpL+1
                jolt += str(fl)
                cnt -= 1
                r = n - cnt + 1
            print(jolt)
            ans += int(jolt)

    print(ans)


solve()