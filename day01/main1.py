with open('input.txt') as file:
    instructions = file.readline().split(", ")
i = 0
j = 0
face = 'N'
for instruction in instructions:
    if face == 'N' and instruction[0] == 'L':
        j -= int(instruction[1:len(instruction)])
        face = 'W'
    elif face == 'N' and instruction[0] == 'R':
        j += int(instruction[1:len(instruction)])
        face = 'E'
    elif face == 'S' and instruction[0] == 'R':
        j -= int(instruction[1:len(instruction)])
        face = 'W'
    elif face == 'S' and instruction[0] == 'L':
        j += int(instruction[1:len(instruction)])
        face = 'E'
    elif face == 'E' and instruction[0] == 'R':
        i += int(instruction[1:len(instruction)])
        face = 'S'
    elif face == 'E' and instruction[0] == 'L':
        i -= int(instruction[1:len(instruction)])
        face = 'N'
    elif face == 'W' and instruction[0] == 'R':
        i -= int(instruction[1:len(instruction)])
        face = 'N'
    elif face == 'W' and instruction[0] == 'L':
        i += int(instruction[1:len(instruction)])
        face = 'S'
print(abs(i)+abs(j))
