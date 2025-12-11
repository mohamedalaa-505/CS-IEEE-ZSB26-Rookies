matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

location_1 = []

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            location_1 = [i + 1, j + 1]
            break

middle_x = 3
middle_y = 3

min_num_of_moves = abs(location_1[0] - middle_x) + abs(location_1[1] - middle_y)

print(min_num_of_moves)

