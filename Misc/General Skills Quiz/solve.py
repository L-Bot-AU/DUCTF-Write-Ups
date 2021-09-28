import socket
from urllib.parse import unquote
from base64 import b64decode as d
from base64 import b64encode as e
import codecs
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pwn-2021.duc.tf", 31905))
s.recv(1024)
s.send(b"\n")
s.recv(1024)
# Addition
s.send(b"2\n")
k = s.recv(1024)

# Hexadecimal manipulation
s.send(bytes(f"{int(k[-3:-1], 16)}\n", "utf-8"))
s.send(bytes(chr(int(s.recv(1024)[-3:-1], 16)) + "\n", "utf-8"))

# URL encoding
s.send(bytes(unquote(str(s.recv(1024)).split(": ", 1)[1][:-3]) + "\n", "utf-8"))

# Base 64
s.send(d(s.recv(2048).decode("utf-8").split(": ", 1)[1]) + b"\n")
s.send(e(bytes(s.recv(2048).decode("utf-8").split(": ")[1][:-1], "utf-8")) + b"\n")

# ROT13
k = s.recv(1024)
a = k.decode('utf-8').split(": ", 1)[1][:-1]
s.send(bytes(codecs.encode(a, "rot_13"), "utf-8") + b"\n")
k = s.recv(1024)
a = k.decode('utf-8').split(": ", 1)[1][:-1]
s.send(bytes(codecs.encode(a, "rot_13"), "utf-8") + b"\n")

# Binary
s.send(bytes(str(int(s.recv(1024).decode("utf-8").split(": ", 1)[1][:-1], 2)), "utf-8") + b"\n")
s.send(bytes(bin(int(s.recv(1024).decode("utf-8").split(": ", 1)[1][:-1])), "utf-8") + b"\n")

# DUCTF :P
s.recv(1024)
s.send(b"DUCTF\n")
print(s.recv(1024))
