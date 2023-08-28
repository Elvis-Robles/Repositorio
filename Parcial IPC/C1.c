#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Funcion para lanzar un dado
int lanzarDado() {
    return rand() % 6 + 1;
}

int main() {
    srand(time(NULL));

    FILE *archivo = fopen("salida.txt", "a");
    if (archivo == NULL) {
        printf("No se pudo abrir el archivo.");
        return 1;
    }

    int suma, resultado, lanzamientos = 0;

    do {
        int dado1 = lanzarDado();
        int dado2 = lanzarDado();
        suma = dado1 + dado2;
        lanzamientos++;

        if (lanzamientos == 1) {
            fprintf(archivo, "Historial de lanzamientos:\n");
        }

        fprintf(archivo, "Lanzamiento %d: %d + %d = %d\n", lanzamientos, dado1, dado2, suma);

        if (suma == 8) {
            resultado = 1;
            fprintf(archivo, "¡Ganaste!\n");
            break;
        } else if (suma == 7) {
            resultado = -1;
            fprintf(archivo, "Perdiste al obtener 7.\n");
            break;
        }

        if (lanzamientos > 1) {
            fprintf(archivo, "Sigue lanzando...\n");
        }
    } while (1);

    fclose(archivo);

    // Mostrar historial de lanzamientos
    char linea[100];
    archivo = fopen("salida.txt", "r");
    if (archivo == NULL) {
        printf("No se pudo abrir el archivo.");
        return 1;
    }

    printf("Historial de lanzamientos:\n");
    while (fgets(linea, sizeof(linea), archivo)) {
        printf("%s", linea);
    }

    fclose(archivo);

    return 0;
}
