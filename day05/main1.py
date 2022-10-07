import hashlib
input = "abbhdwsy"
count = 0
password = ""
for i in range(8):
    while True:
        result = hashlib.md5((input + str(count)).encode()).hexdigest()
        count += 1
        if result[:5] == "00000":
            password += result[5]
            break
print(password)
