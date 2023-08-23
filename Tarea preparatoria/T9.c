#include <stdio.h>

int main() {
    int N;
    
    printf("Ingrese el valor de N: ");
    scanf("%d", &N);
    
    int fib[N];
    
    fib[0] = 0;
    fib[1] = 1;
    
    for (int i = 2; i < N; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    
    printf("Los primeros %d terminos de la serie de Fibonacci son:\n", N);
    for (int i = 0; i < N; i++) {
        printf("%d ", fib[i]);
    }
    
    return 0;
}
