t = int(input())


for i in range(t):
    n = int(input())
    s = input().upper()
    problems = []
    ballones = 0
    for j in s:
        if j in problems:
            ballones += 1
        else:
            ballones += 2
            problems.append(j)
    print(ballones)