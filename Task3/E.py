def function(a, b):
    s1 = str(a) * b
    s2 = str(b) * a
    return min(s1, s2)

a, b = map(int, input().split())
print(function(a, b))