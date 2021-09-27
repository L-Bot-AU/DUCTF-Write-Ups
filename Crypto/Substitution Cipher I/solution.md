# Challenge

Just a simple substitution cipher to get started...

```sage
# substitution-cipher-i.sage:
def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P.<x> = PolynomialRing(ZZ)
f = 13*x^2 + 3*x + 7

FLAG = open('./flag.txt', 'rb').read().strip()

enc = encrypt(FLAG, f)
print(enc)
```

```
# output.txt:
𖿫𖝓玲𰆽𪃵𢙿疗𫢋𥆛🴃䶹𬑽蒵𜭱𫢋𪃵蒵🴃𜭱𩕑疗𪲳𜭱窇蒵𱫳
```

# Solution

In the challenge statement we are provided with two files, substitution-cipher-i.sage and output.txt. substitution-cipher-i.sage contained a polynomial
`f = 13x^2 + 3x + 7` mapping integers to integers, while the actual `encrypt` function itself encrypts the message by changing each character `c` to the
character with unicode value `f(c)`. This produces the string of unreadable characters in `output.txt`.

In the solution [code](https://github.com/L-Bot-SBHS/DUCTF-Write-Ups/new/master/Crypto/Substitution%20Cipher%20I/sub-cipher-i.py), we open the file with utf-8
encoding. To find the flag, we loop through the characters, and apply the inverse of f to the integer representation (ord) of each character. We can find the roots
of the quadratic formula 13x^2 + 3x + 7 = a through the positive branch of the quadratic formula, x = (-3 + sqrt(9 + 52(a - 7))) / 26. Concatenating the ASCII
value of each solution represents gives us the flag:

DUCTF{sh0uld'v3_us3d_r0t_13}
