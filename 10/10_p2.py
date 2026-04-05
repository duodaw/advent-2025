from scipy.optimize import linprog

def solve():
    with open('10/10.txt', 'r') as file:
        ans = 0
        for line in file:
            joltage, buttons, diagram = parse(line)
            ans += f(joltage, buttons)
        return ans


def f(joltage, buttons):
    A = []
    for i in buttons:
        B = [0 for _ in range(len(joltage))]
        for j in i:
            B[j] += 1
        A.append(B)
    D = []
    for i in range(len(joltage)):
        C = []
        for j in A:
            C.append(j[i])
        D.append(C)
    c = [1] * len(buttons)
    x = linprog(c, A_ub=None, b_ub=None, A_eq=D, b_eq=joltage,
            bounds=(0, None), method='highs', integrality=True)
    return int(x.fun)

def parse(line):
    buttons = []
    joltage = []
    diagram = ""
    A = line.strip().split()
    for i in A:
        if i[0] == '(':
            buttons.append([int(x) for x in  i[1:-1].split(",")])
        elif i[0] == '{':
            joltage = [int(x) for x in i[1:-1].split(",")]
            return joltage, buttons, diagram
        elif i[0]=='[':
            diagram =  i[1:-1]

print(solve())
