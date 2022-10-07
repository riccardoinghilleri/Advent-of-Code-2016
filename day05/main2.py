import hashlib
input = "abbhdwsy"
count = 0
password = ['*', '*', '*', '*', '*', '*', '*', '*']
for i in range(8):
    while True:
        result = hashlib.md5((input + str(count)).encode()).hexdigest()
        count += 1
        if result[:5] == "00000" and result[5].isdigit() and 0 <= int(result[5]) <= 7 and password[int(result[5])] == '*':
            password[int(result[5])] = result[6]
            break
print("".join(password))
