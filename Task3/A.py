import math

def attacks_needed(H, A):
    return math.ceil(H / A)

H, A = map(int, input().split())
print(attacks_needed(H, A))