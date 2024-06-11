CC=gcc
CFLAGS=-m32 -no-pie -fno-stack-protector
LDFLAGS=-z noexecstack

SRC=main.c
OBJ=main.o
BIN=ex3

$(BIN): $(OBJ)
	@echo "Compiling..."
	$(CC) -o $@ $(SRC) $(LDFLAGS) $(CFLAGS)
