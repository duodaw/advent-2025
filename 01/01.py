import sys
import math

def solve():
    n = 50
    ans = 0
    with open('1.txt', 'r') as file:
        for line in file:
            line = line.strip()
            p = line[-2:] if len(line) > 2 else line[-1:]
            if line[0] == 'L':
                n = n - int(p)
            else:
                n = n + int(p)
            if n < 0:
                n += 100
            elif n>99:
                n-=100
            if n == 0:
                ans+= 1
    print(ans)

solve()