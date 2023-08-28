#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Función para calcular la media
float calcularMedia(int calificaciones[], int n) {
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += calificaciones[i];
    }
    return (float)suma / n;
}

// Función para calcular la mediana
float calcularMediana(int calificaciones[], int n) {
    // Primero ordenamos el arreglo
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (calificaciones[j] > calificaciones[j + 1]) {
                int temp = calificaciones[j];
                calificaciones[j] = calificaciones[j + 1];
                calificaciones[j + 1] = temp;
            }
        }
    }

    if (n % 2 == 0) {
        return (float)(calificaciones[n / 2 - 1] + calificaciones[n / 2]) / 2;
    } else {
        return calificaciones[n / 2];
    }
}

// Función para calcular la moda
int calcularModa(int calificaciones[], int n) {
    // Implementar el cálculo de la moda aquí
    // Retorna el valor de la moda
}

// Función para calcular el rango
int calcularRango(int calificaciones[], int n) {
    int max = calificaciones[0];
    int min = calificaciones[0];

    for (int i = 1; i < n; i++) {
        if (calificaciones[i] > max) {
            max = calificaciones[i];
        }
        if (calificaciones[i] < min) {
            min = calificaciones[i];
        }
    }

    return max - min;
}

// Función para calcular la desviación estándar
float calcularDesviacionEstandar(int calificaciones[], int n, float media) {
    // Implementar el cálculo de la desviación estándar aquí
    // Retorna el valor de la desviación estándar
}

// Función para calcular la varianza
float calcularVarianza(int calificaciones[], int n, float media) {
    // Implementar el cálculo de la varianza aquí
    // Retorna el valor de la varianza
}

int main() {
    int n = 5;  // Número de calificaciones
    int calificaciones[n];

    // Leer las calificaciones del usuario
    for (int i = 0; i < n; i++) {
        printf("Ingrese la calificacion %d: ", i + 1);
        scanf("%d", &calificaciones[i]);
    }

    // Calcular estadísticos
    float media = calcularMedia(calificaciones, n);
    float mediana = calcularMediana(calificaciones, n);
    int moda = calcularModa(calificaciones, n);
    int rango = calcularRango(calificaciones, n);
    float desviacionEstandar = calcularDesviacionEstandar(calificaciones, n, media);
    float varianza = calcularVarianza(calificaciones, n, media);

    // Mostrar resultados
    printf("Media: %.2f\n", media);
    printf("Mediana: %.2f\n", mediana);
    printf("Moda: %d\n", moda);
    printf("Rango: %d\n", rango);
    printf("Desviacion Estandar: %.2f\n", desviacionEstandar);
    printf("Varianza: %.2f\n", varianza);

    // Almacenar resultados en un archivo de texto
    FILE *archivo = fopen("salida.txt", "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    fprintf(archivo, "Media: %.2f\n", media);
    fprintf(archivo, "Mediana: %.2f\n", mediana);
    fprintf(archivo, "Moda: %d\n", moda);
    fprintf(archivo, "Rango: %d\n", rango);
    fprintf(archivo, "Desviacion Estandar: %.2f\n", desviacionEstandar);
    fprintf(archivo, "Varianza: %.2f\n", varianza);

    fclose(archivo);

    // Opción de visualizar el historial de datos
    char opcion;
    printf("¿Desea visualizar el historial de datos? (S/N): ");
    scanf(" %c", &opcion);

    if (opcion == 'S' || opcion == 's') {
        archivo = fopen("salida.txt", "r");
        if (archivo == NULL) {
            printf("Error al abrir el archivo.\n");
            return 1;
        }

        char caracter;
        while ((caracter = fgetc(archivo)) != EOF) {
            printf("%c", caracter);
        }

        fclose(archivo);
    }

    return 0;
}
