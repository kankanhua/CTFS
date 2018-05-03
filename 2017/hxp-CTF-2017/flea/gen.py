#!/usr/bin/env python3
import random, gmpy2
random = random.SystemRandom()

bits = 2048

p = gmpy2.next_prime(random.randrange(1 << bits // 2))
q = gmpy2.next_prime(random.randrange(1 << bits // 2))

n = p * q
l = (p ^ q) * (p + q)

flag = open('flag.txt', 'rb').read()
m = int.from_bytes(flag, 'big')

with open('data.txt', 'w') as f:
    f.write('{:#x}\n'.format(n))
    f.write('{:#x}\n'.format(l))
    f.write('{:#x}\n'.format(pow(m, 65537, n)))

