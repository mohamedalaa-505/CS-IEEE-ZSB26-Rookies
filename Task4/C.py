def solve(i, sum1, sum2):
    if i == n:
        return abs(sum1 - sum2)

    diff1 = solve(i + 1, sum1 + apples[i], sum2)
    diff2 = solve(i + 1, sum1, sum2 + apples[i])

    return min(diff1, diff2)


n = int(input())
apples = list(map(int, input().split()))

print(solve(0, 0, 0))