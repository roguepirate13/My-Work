m = 16
for i in range(m, 0, -1):
    for j in range(0, m - i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()
n = 16
for i in range(0, 16):
    print(' '*n, end='')
    print('* ' * i)
    n -= 1
