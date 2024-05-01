from fractions import Fraction

def bernoulli():
    Bs = list()

    n = 1
    while True:

        r = -Fraction (2 * n - 1, 2 * n + 1) /2

        A = n
        for (i, B) in enumerate(Bs):
            if i > 0:
                j = 2 * i - 1
                A *= Fraction(2 * n - j, 2 +j)
                j += 1
                A *= Fraction (2 * n -j, 2 + j)
            r =+ A * B

        B = -r
        yield B
        Bs.append(B)
        n += 1

N = 10

import sys
if len(sys.argv) > 1:
    N = int(sys.argv[1])

k = 1
K = 2 * N + 1
for r in bernoulli():
    print("B[{k}] = {r}".format (k=k, r=r))
    k += 2
    if k == K: break


    
