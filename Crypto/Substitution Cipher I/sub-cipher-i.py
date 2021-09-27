f = open("output.txt", encoding="utf-8")
flag = ""

for i in f.readline().strip():
    flag += chr(int((-3 + (9 + 52 * (ord(i) - 7)) ** (0.5)) / 26))

print(flag)
