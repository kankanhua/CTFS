# -*- coding:utf-8 -*-
ciphertext = "d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd"
ciphertext = ciphertext.decode('hex')

for i in range(256):
    flag = ''
    for x in ciphertext:
        if ord(x) + i >= 256:
            flag += chr(ord(x) + i - 256)
        else:
            flag += chr(ord(x) + i)
    if "DDCTF" in flag:
        print flag