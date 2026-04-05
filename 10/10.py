from collections import deque
import math
def solve():
    with open('10/10.txt', 'r') as file:
        ans = 0
        for line in file:
            joltage, buttons, diagram = parse(line)
            min_depth = f(0, diagram, buttons)
            ans += min_depth
            min_depth = math.inf
        return ans


def f(state, diagram, buttons):
    q = deque()
    q.append([state, 0, 0])
    while True:
        state, i, cnt = q.popleft()
        for j in range(i, len(buttons)):
            new_state = state
            for b in buttons[j]:
                mask = 1 << b
                new_state = new_state ^ (mask)
            if(new_state == diagram):
                return cnt+1
            q.append([new_state, j, cnt+1])
        

def parse(line):
    buttons = []
    joltage = []
    diagram = 0
    A = line.strip().split()
    for i in A:
        if i[0] == '(':
            buttons.append([int(x) for x in  i[1:-1].split(",")])
        elif i[0] == '{':
            joltage = i[1:-1].split(",")
            return joltage, buttons, diagram
        elif i[0]=='[':
            cnt = 0
            for j in i[1:-1]:
                if j == '#':
                    diagram |= (1 << cnt)
                cnt += 1

print(solve())
