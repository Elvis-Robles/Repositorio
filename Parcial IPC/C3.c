#include <stdio.h>

int main() {
    float precio, iva, precioSinIVA;
    const float tasaIVA = 0.12;  // 12% de IVA

    // Solicitar al usuario el ingreso del precio en quetzales
    printf("Ingrese el precio en quetzales: ");
    scanf("%f", &precio);

    // Calcular el IVA y el precio sin IVA
    iva = precio * tasaIVA;
    precioSinIVA = precio - iva;

    // Mostrar los resultados
    printf("Total IVA: %.2f quetzales\n", iva);
    printf("Precio sin IVA: %.2f quetzales\n", precioSinIVA);

    // Abrir el archivo en modo de escritura
    FILE *archivo = fopen("salida.txt", "a");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.");
        return 1;
    }

    // Escribir los datos en el archivo
    fprintf(archivo, "Precio ingresado: %.2f quetzales\n", precio);
    fprintf(archivo, "Total IVA: %.2f quetzales\n", iva);
    fprintf(archivo, "Precio sin IVA: %.2f quetzales\n", precioSinIVA);
    fprintf(archivo, "--------------------------\n");

    // Cerrar el archivo
    fclose(archivo);

    return 0;
}
