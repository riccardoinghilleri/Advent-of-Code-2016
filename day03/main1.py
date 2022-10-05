def possible_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


with open('input.txt') as file:
    count = 0
    for line in file:
        if possible_triangle(int(line[:5]), int(line[5:10]), int(line[10:15])):
            count += 1
print(count)
