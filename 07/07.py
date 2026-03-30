def solve():
    with open('07/07.txt', 'r') as file:
        pos = set()
        ans = 0
        for line in file:
            for i in range(len(line.strip())):
                if line[i] == 'S':
                    pos.add(i)
            break
        for line in file:
            to_remove = []
            to_add = []
            for i in pos:
                if line[i] == '^':
                    if i > 0:
                        to_add.append(i-1)
                    if i < len(line.strip()) - 1:
                        to_add.append(i+1)
                    to_remove.append(i)
                    ans += 1
            for i in to_remove:
                pos.remove(i)
            pos.update(to_add)
        print(ans)

solve()