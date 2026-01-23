def digits(N, K):
    count = 0
    while N > 0:
        N //= K
        count += 1
    return count

N, K = map(int, input().split())
print(digits(N, K))