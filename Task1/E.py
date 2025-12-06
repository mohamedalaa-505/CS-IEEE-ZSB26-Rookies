n = int(input())

word = 'codeforces'
for i in range(n):
    letter = input().lower()
    if letter in word:
        print('YES')
    else:
        print('NO')