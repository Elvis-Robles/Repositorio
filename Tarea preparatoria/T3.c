#include <stdio.h>
#include <string.h>

int main() {
    char text[100]; 
    
    printf("Ingrese una cadena de texto: ");
    fgets(text, sizeof(text), stdin);
    
    text[strcspn(text, "\n")] = '\0';
    
    int length = strlen(text);
    
    printf("La cantidad de caracteres en la cadena es: %d\n", length);
    
    return 0;
}