def function(n):
    print(n, end=' ')
    if n == 1:
        return
    if n % 2 == 0:
        function(n // 2)
    else:
        function(3 * n + 1)

n = int(input())
function(n)