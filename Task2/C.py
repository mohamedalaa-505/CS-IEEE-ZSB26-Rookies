<<<<<<< HEAD
n = int(input())

for i in range(n):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
=======
n = int(input())

for i in range(n):
    s = input()
    if len(s) <= 10:
        print(s)
    else:
>>>>>>> 2336f7ec8a38f51be205a3b2b6e95a88d433f73c
        print(s[0] + str(len(s) - 2) + s[-1])