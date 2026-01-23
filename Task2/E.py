<<<<<<< HEAD
n = int(input())
s = ''.join(sorted(input().lower()))

alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0

for ch in s:
    if i < 26 and ch == alphabet[i]:
        i += 1

print("YES" if i == 26 else "No")


=======
n = int(input())
s = ''.join(sorted(input().lower()))

alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0

for ch in s:
    if i < 26 and ch == alphabet[i]:
        i += 1

print("YES" if i == 26 else "No")


>>>>>>> 2336f7ec8a38f51be205a3b2b6e95a88d433f73c
