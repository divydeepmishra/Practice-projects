#include <cs50.h>
#include <stdio.h>
void print_row(int spaces, int bricks, int slash, int lenght);
int main(void)
{
    int n;
    do
    {
        n = get_int("Height:  ");
    }
    while (n < 1 || n > 8);
    for (int i = 0; i < n; i++)
    {
        print_row(n, i + 1, n, i + 1);
    }
}
void print_row(int spaces, int bricks, int slash, int lenght)
{
    for (int j = 0; j < spaces - bricks; j++)
    {
        printf(" ");
    }
    for (int j = 0; j < bricks; j++)
    {
        printf("#");
    }
    for (int j = 0; j < 2; j++)
    {
        printf(" ");
    }
    for (int j = 0; j < lenght; j++)
    {
        printf("#");
    }
    printf("\n");
}
