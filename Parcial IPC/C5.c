#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nombre[50];
    int puntos;
} Jugador;

int jugarAdivinanzas() {
    int aciertos = 0;
    // Aquí podrías poner las adivinanzas y el código para jugar
    // Incrementar "aciertos" cada vez que el usuario adivine correctamente
    return aciertos;
}

void verHistorial(Jugador jugadores[], int numJugadores) {
    printf("Historial de Jugadores:\n");
    for (int i = 0; i < numJugadores; i++) {
        printf("Nombre: %s - Puntos: %d\n", jugadores[i].nombre, jugadores[i].puntos);
    }
}

int main() {
    Jugador jugadores[100];
    int numJugadores = 0;

    int opcion;
    do {
        printf("\nMenu:\n");
        printf("1. Jugar a las adivinanzas\n");
        printf("2. Ver el historial de jugadores\n");
        printf("3. Borrar historial\n");
        printf("4. Salir\n");
        printf("Selecciona una opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                printf("Cuantos puntos obtendras!\n");
                int aciertos = jugarAdivinanzas();

                // Pedir el nombre del jugador
                printf("Ingresa tu nombre: ");
                scanf("%s", jugadores[numJugadores].nombre);

                // Pedir los puntos al jugador
                printf("Ingresa tus puntos: ");
                scanf("%d", &jugadores[numJugadores].puntos);

                numJugadores++;

                FILE *archivo = fopen("salida.txt", "a");
                if (archivo != NULL) {
                    fprintf(archivo, "%s %d\n", jugadores[numJugadores - 1].nombre, jugadores[numJugadores - 1].puntos);
                    fclose(archivo);
                } else {
                    printf("Error al abrir el archivo.\n");
                }
                break;

            case 2:
                verHistorial(jugadores, numJugadores);
                break;

            case 3:
                remove("salida.txt");
                printf("Historial borrado.\n");
                break;

            case 4:
                printf("Saliendo del programa.\n");
                break;

            default:
                printf("Opcion invalida.\n");
                break;
        }
    } while (opcion != 4);

    return 0;
}
