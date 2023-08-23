#include <stdio.h>

int main() {
    char texto[100], duplicado[200];
    int i, j = 0;
    
    printf("Ingrese una cadena de texto: ");
    fgets(texto, 100, stdin);
    
    for (i = 0; texto[i] != '\0' && texto[i] != '\n'; i++) {
        duplicado[j++] = texto[i];
        duplicado[j++] = texto[i];
    }
    duplicado[j] = '\0';
    
    printf("Cadena duplicada: %s\n", duplicado);
    
    return 0;
}
