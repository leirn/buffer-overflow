#include <string.h>

void foo(char * input)
{
    char buf[16];

    strcpy(buf, input);
}

int main(int argc, char ** argv)
{
    foo(argv[1]);
    return 0;
}
