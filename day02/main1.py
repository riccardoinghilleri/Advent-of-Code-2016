matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
with open('input.txt') as file:
    i = 1
    j = 1
    for line in file.readlines():
        for char in line:
            if char == 'L':
                j = max(0, j - 1)
            elif char == 'R':
                j = min(2, j + 1)
            elif char == 'U':
                i = max(0, i - 1)
            elif char == 'D':
                i = min(2, i + 1)
        print(matrix[i][j])

