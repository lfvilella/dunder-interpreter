#include <stdio.h>

int simple_sum() {
    int a = 10;
    int b = 10;
    int c = a + b;
    return c;
}

int main() {
    int sum = simple_sum();
    printf("%d\n", sum);
    return 0;
}
