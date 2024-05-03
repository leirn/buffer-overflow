#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>

int main()
{

    int other_data = 0;
    int check = 0x01020304;
    char buf[16];

    printf("Enter a string:\n");
    fgets(buf, 21, stdin);

    printf("\n[buf]: %s\n", buf);
    printf("[check] %p\n", check);

    if (check == 0x1ee7c0de)
    {
        printf("\nGood game!\n");
    }
    else if ((check != 0x1ee7c0de) && (check != 0x01020304))
    {
        printf("\nAlmost there\n");
    }
    else {
        printf("\nTry again\n");
    }

    return 0;
}
