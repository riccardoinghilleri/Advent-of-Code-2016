with open('input.txt') as file:
    instructions = file.readline().split(", ")
i = 0
j = 0
face = 'N'
path = [(0, 0)]
found = False
for instruction in instructions:
    if not found:
        if face == 'N' and instruction[0] == 'L':
            for num in range(int(instruction[1:len(instruction)])):
                j -= 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'W'
        elif face == 'N' and instruction[0] == 'R':
            for num in range(int(instruction[1:len(instruction)])):
                j += 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'E'
        elif face == 'S' and instruction[0] == 'R':
            for num in range(int(instruction[1:len(instruction)])):
                j -= 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'W'
        elif face == 'S' and instruction[0] == 'L':
            for num in range(int(instruction[1:len(instruction)])):
                j += 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'E'
        elif face == 'E' and instruction[0] == 'R':
            for num in range(int(instruction[1:len(instruction)])):
                i += 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'S'
        elif face == 'E' and instruction[0] == 'L':
            for num in range(int(instruction[1:len(instruction)])):
                i -= 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'N'
        elif face == 'W' and instruction[0] == 'R':
            for num in range(int(instruction[1:len(instruction)])):
                i -= 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'N'
        elif face == 'W' and instruction[0] == 'L':
            for num in range(int(instruction[1:len(instruction)])):
                i += 1
                if (i, j) in path:
                    found = True
                    break
                path.append((i, j))
            face = 'S'
    else:
        break
print(abs(i)+abs(j))
