def function(X, Y):
    if X % 5 == 0 and Y >= X + 0.50:
        Y -= (X + 0.50)
    return f"{Y:.2f}"

X, Y = map(float, input().split())
print(function(X, Y))