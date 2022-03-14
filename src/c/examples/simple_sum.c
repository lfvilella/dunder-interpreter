#include <stdio.h>

int simple_sum() {
    int a = 1;
    int b = 1;
    int c = a + b;
    return c;
}

int main() {
    int sum = simple_sum();
    printf("%d\n", sum);
    return 0;
}
