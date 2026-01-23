<<<<<<< HEAD
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] == a[1]:
        common = a[0]
    else:
        common = a[2]
    for j in range(n):
        if a[j] != common:
            print(j + 1)


=======
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] == a[1]:
        common = a[0]
    else:
        common = a[2]
    for j in range(n):
        if a[j] != common:
            print(j + 1)


>>>>>>> 2336f7ec8a38f51be205a3b2b6e95a88d433f73c
