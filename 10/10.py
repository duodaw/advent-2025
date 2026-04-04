from collections import deque
import math
def solve():
    with open('10/10.txt', 'r') as file:
        ans = 0
        for line in file:
            global min_depth
            diagram, buttons = parse(line)
            state = 0
            min_depth = f(state, diagram, buttons)
            print(min_depth)
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
    diagram = 0
    buttons = []
    button = []
    in_diag = True
    cnt = -1
    for i in line:
        cnt += 1
        if i == '[' or i=='(' or i == ',' or i.strip()=='':
            continue
        if i == ']':
            in_diag = False
            continue
        elif in_diag:
            if i == '#':
                diagram |= (1 << cnt-1)
        elif i == '{':
            break
        elif i == '(':
            continue
        elif i == ')':
            buttons.append(button)
            button = []
        else:
            button.append(int(i))
    return diagram, buttons

print(solve())
