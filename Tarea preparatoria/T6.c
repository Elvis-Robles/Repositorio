#include <stdio.h>

int main() {
    int inicio, final, i, cont = 0;
    
    printf("Ingrese el numero inicial: ");
    scanf("%d", &inicio);
    
    printf("Ingrese el numero final: ");
    scanf("%d", &final);
    
    for (i = inicio; i <= final; i++) {
        if (i % 2 == 0) {
            cont++;
        }
    }
    
    printf("Hay %d numeros pares en el rango [%d, %d]\n", cont, inicio, final);
    
    return 0;
}