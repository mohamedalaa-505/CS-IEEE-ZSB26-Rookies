n = int(input())
s = ''.join(sorted(input().lower()))

alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0

for ch in s:
    if i < 26 and ch == alphabet[i]:
        i += 1

print("YES" if i == 26 else "No")


