#include <stdio.h>

int main(void) 
{
    int n = 5;
    int fib = 0;
    int aux = 0;    

    while(fib < 1000)
    { 
        printf("%d-", fib);                   
        fib = fib + aux;                 
        aux = n;
        n = fib;        
    }
  printf("\n");
  return 0;
}