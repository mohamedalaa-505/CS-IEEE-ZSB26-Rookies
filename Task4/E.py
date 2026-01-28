def permute(i):
    if i == n:
        res.add("".join(s))
        return

    for j in range(i, n):
        s[i], s[j] = s[j], s[i]
        permute(i + 1)
        s[i], s[j] = s[j], s[i]


s = list(input().strip())
n = len(s)

res = set()
permute(0)

ans = sorted(res)

print(len(ans))
for x in ans:
    print(x)