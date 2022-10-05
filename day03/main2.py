def possible_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


with open('input.txt') as file:
    count = 0
    index = 0
    triangles = file.readlines()
    while index < len(triangles) - 2:
        if possible_triangle(int((triangles[index])[:5]), int((triangles[index + 1])[:5]), int((triangles[index + 2])[:5])):
            count += 1
        if possible_triangle(int((triangles[index])[5:10]), int((triangles[index + 1])[5:10]), int((triangles[index + 2])[5:10])):
            count += 1
        if possible_triangle(int((triangles[index])[10:15]), int((triangles[index + 1])[10:15]), int((triangles[index + 2])[10:15])):
            count += 1
        index += 3
print(count)
