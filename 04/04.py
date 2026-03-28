
def solve():
    ans = 0
    with open('04.txt', 'r') as file:
        L = []
        for line in file:
            L.append(line.strip())
        
        for i in range(len(L)):
            for j in range(len(L[i])):
                if(L[i][j] == '@' and access(L, i-1, j) + access(L, i-1, j+1) + access(L, i-1, j-1)
                   + access(L, i+1, j)+ access(L, i+1, j-1)+ access(L, i+1, j+1)
                   + access(L, i, j+1) + access(L, i, j-1) < 4):
                    ans+= 1
    return ans

def access(L, i, j):
    if i<0 or j<0 or i>=len(L) or j>=len(L[i]) or L[i][j] != '@':
        return 0

    return 1


print(solve())