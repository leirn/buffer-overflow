#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
 
void wrong_way() {
    printf("You are not supposed to be here\n");
}
 
void right_way() {
    printf("Normal execution flow\n");
}
 
void main()
{
    int var;
    void (*func)()=right_way;
    char buf[120];
    printf("Tell me something you like:\n");
    fgets(buf,125,stdin);
    func();
}