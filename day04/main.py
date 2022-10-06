def max_frequency(a):
    ascii = []
    for i in range(5):
        max = 0
        for elem in a:
            if elem > max:
                max = elem
        ascii.append(a.index(max) + 97)
        a[a.index(max)] = -1
    return ascii


def decrypt(id):
    chars_list = []
    for i in range(26):
        chars_list.append(chr((i + id) % 26 + 97))
    return chars_list


with open('input.txt') as file:
    real_rooms = []
    sum = 0
    for line in file:
        frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        index = 0
        checksum = line[len(line) - 7: len(line) - 2]
        for index in range(len(line)):
            if line[index] != '-' and not line[index: len(line) - 8].isdigit():
                frequency[ord(line[index]) - 97] += 1
            elif line[index: len(line) - 8].isdigit():
                room_id = int(line[index: len(line) - 8])
                break
        res = max_frequency(frequency)
        test = chr(res[0]) + chr(res[1]) + chr(res[2]) + chr(res[3]) + chr(res[4])
        if checksum == test:
            sum += room_id
            real_rooms.append(line[:len(line) - 8])  # part 2
print(sum)
for elem in real_rooms:
    room_id = elem[len(elem) - 3: len(elem)]
    elem = elem[: len(elem) - 3]
    elem = elem.replace('-', ' ')
    decrypted_list = decrypt(int(room_id))
    for i in range(len(elem)):
        if elem[i] != ' ':
            l = list(elem)
            l[i] = decrypted_list[ord(l[i]) - 97]
            elem = "".join(l)
    if elem == "northpole object storage ":
        print(room_id)
        break
