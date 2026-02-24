for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x = i
        y = row.index(1)
 
print(abs(x - 2) + abs(y - 2))
