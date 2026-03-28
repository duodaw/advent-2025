
def solve():
    with open('05.txt', 'r') as file:
        ans = 0
        ranges = []
        for line in file:
            if len(line.strip()) == 0:
                break
            ranges.append([int(x) for x in line.strip().split('-')])
            
        ranges = sorted(ranges, key=lambda x: x[0])
        separate_ranges = []
        separate_ranges.append(ranges[0])
        for i in range(1, len(ranges)):
            if ranges[i][0] <= separate_ranges[len(separate_ranges)-1][1]:
                if ranges[i][1] > separate_ranges[len(separate_ranges)-1][1]:
                    separate_ranges[len(separate_ranges)-1][1] = ranges[i][1]
            else:
                separate_ranges.append(ranges[i])
        for i in separate_ranges:
            ans += i[1]-i[0]+1
        print(ans)
solve()