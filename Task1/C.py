n = int(input())

for i in range(n):
    rate = int(input())
    if rate >= 1900:
        print('Division 1')
    elif 1600 <= rate <= 1899:
        print('Division 2')
    elif 1400 <= rate <= 1599:
        print('Division 3')
    elif rate <= 1399:
        print('Division 4')