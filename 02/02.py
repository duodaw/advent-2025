def solve():
    with open('02.txt', 'r') as file:
        input = file.readline().strip()
        ans = 0
        L = input.split(',')
        for i in L:
            [l, r] = i.split('-')
            l = int(l)
            r = int(r)
            while l <= r:
                n = len(str(l))
                if (n % 2 == 0) and (str(l)[0:n//2] == str(l)[n//2:]):
                    ans += l
                l += 1
        print(ans)

solve()