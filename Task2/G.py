<<<<<<< HEAD
q = int(input())

for i in range(q):
    n = int(input())
    s, t = input().split()

    if len(s) != n or len(t) != n:
        continue

    if sorted(s) == sorted(t):
        print('YES')
    else:
=======
q = int(input())

for i in range(q):
    n = int(input())
    s, t = input().split()

    if len(s) != n or len(t) != n:
        continue

    if sorted(s) == sorted(t):
        print('YES')
    else:
>>>>>>> 2336f7ec8a38f51be205a3b2b6e95a88d433f73c
        print('NO')