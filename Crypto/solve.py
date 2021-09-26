import socket
from base64 import b64decode as d
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pwn-2021.duc.tf", 31914))
s.recv(2048)
key = b"!_S"
for i in range(3, 16):
    for check_char in range(128):
        payload = b"0"*(15-i)+key+bytes([check_char])+b"0"*(15-i)
        s.send(payload + b"\n")
        response = s.recv(2048).decode("utf-8").split("\n", 1)[0]
        out = d(response)
        if out[32:48] == out[48:64]: # 32 byte flag. 33rd to 48th and 49th to 64th should be the same
            break
    else:
        print(key[:-1])
        break
    key += bytes([check_char - 1])
print("Final:", key)
