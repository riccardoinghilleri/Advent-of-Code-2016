matrix = [['!', '!', 1, '!', '!'], ['!', 2, 3, 4, '!'], [5, 6, 7, 8, 9],
          ['!', 'A', 'B', 'C', '!'], ['!', '!', 'D', '!', '!']]
with open('input.txt') as file:
    i = 2
    j = 0
    for line in file.readlines():
        for char in line:
            if char == 'L':
                j = max(0, j - 1)
                if matrix[i][j] == '!':
                    j += 1
            elif char == 'R':
                j = min(4, j + 1)
                if matrix[i][j] == '!':
                    j -= 1
            elif char == 'U':
                i = max(0, i - 1)
                if matrix[i][j] == '!':
                    i += 1
            elif char == 'D':
                i = min(4, i + 1)
                if matrix[i][j] == '!':
                    i -= 1
        print(matrix[i][j])

