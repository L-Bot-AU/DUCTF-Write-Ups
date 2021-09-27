from string import ascii_lowercase, digits
import numpy as np
import sys

CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits

n = 6
x = np.zeros(n)
a = np.array([[ 1,  1,  1,  1,  1,  1, 19],
       [17, 32, 16,  8,  4,  2, 34],
       [24,  8, 34, 27,  9,  3, 32],
       [ 7, 37, 21, 17, 16,  4, 41],
       [21, 23, 14, 31, 25,  5, 13],
       [32, 21, 27, 28, 36,  6, 40]])

# Applying Gauss Elimination
for i in range(n):
    for j in range(i+1, n):
        ratio = (a[j][i] * pow(int(a[i][i]), -1, 47)) %47
        
        for k in range(n+1):
            a[j][k] = (a[j][k] - ratio * a[i][k])%47

# Back Substitution
x[n-1] = (a[n-1][n] * pow(int(a[n-1][n-1]), -1, 47))%47

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = (x[i] - a[i][j]*x[j])%47
    
    x[i] = (x[i] * pow(int(a[i][i]), -1, 47))%47

# above code from https://www.codesansar.com/numerical-methods/gauss-elimination-method-python-program.htm
# with modifications to make it work in GF(47)

def p(x):
	return (41*x**6 + 15 * x**5 + 40 * x **4 + 9 * x **3 + 28 * x**2 + 27 * x+ 1) % 47

coefs = list(map(int, x))
with open("output.txt") as f:
    l = f.readline().strip()
    for char in l:
        Q = CHARSET.index(char)
        for i in range(47):
            if p(i) == Q:
                break
        print(CHARSET[i], end="")
