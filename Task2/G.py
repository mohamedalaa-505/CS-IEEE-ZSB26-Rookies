q = int(input())

for i in range(q):
    n = int(input())
    s, t = input().split()

    if len(s) != n or len(t) != n:
        continue

    if sorted(s) == sorted(t):
        print('YES')
    else:
        print('NO')