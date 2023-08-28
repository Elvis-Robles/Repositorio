#include <stdio.h>
#include <stdbool.h>

// Función para verificar si un número es primo
bool esPrimo(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int numero;
    printf("Ingrese un numero: ");
    scanf("%d", &numero);

    bool primo = esPrimo(numero);

    FILE *archivo = fopen("salida.txt", "a");  // Abre el archivo en modo de agregar
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    if (primo) {
        printf("%d es un numero primo.\n", numero);
        fprintf(archivo, "%d es un número primo.\n", numero);
    } else {
        printf("%d es un numero compuesto.\n", numero);
        fprintf(archivo, "%d es un número compuesto.\n", numero);
    }

    fclose(archivo);

    // Mostrar historial
    printf("\nHistorial de datos:\n");
    archivo = fopen("salida.txt", "r");  // Abre el archivo en modo de lectura
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    char linea[100];
    while (fgets(linea, sizeof(linea), archivo)) {
        printf("%s", linea);
    }

    fclose(archivo);

    return 0;
}
