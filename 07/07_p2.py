def solve():
    with open('07/07.txt', 'r') as file:
        pos_count = {}
        for line in file:
            for i in range(len(line.strip())):
                if line[i] == 'S':
                    pos_count[i] = 1
            break
        for line in file:
            tmp_pos_count = pos_count.copy()
            for i in pos_count:
                if line[i] == '^':
                    if i > 0:
                        if i-1 in tmp_pos_count:
                            tmp_pos_count[i-1]+= pos_count[i]
                        else:
                            tmp_pos_count[i-1] = pos_count[i]
                    if i < len(line.strip()) - 1:
                        if i+1 in tmp_pos_count:
                            tmp_pos_count[i+1]+= pos_count[i]
                        else:
                            tmp_pos_count[i+1] = pos_count[i]
                    del tmp_pos_count[i]
            pos_count = tmp_pos_count.copy()
        ans = 0
        for pos in pos_count:
            ans += pos_count[pos]
        print(ans)

solve()