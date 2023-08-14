#include <stdio.h>

/*
    Este programa genera una calculadora basica
*/

int main() {
    int op, uno, dos;
    do {
        printf(" --- calculadora ---\n");
        printf("\n¿Qué desea hacer?\n");
        printf("1) Sumar\n");
        printf("2) Restar\n");
        printf("3) Multiplicar\n");
        printf("4) Dividir\n");
        printf("5) Salir\n");
        scanf("%d", &op);

        switch (op) {
            case 1:
                printf("\tSumar\n");
                printf("Introduzca los numeros a sumar separados por comas\n");
                scanf("%d,%d", &uno, &dos);
                printf("%d + %d = %d\n", uno, dos, (uno + dos));
                break;
            case 2:
                printf("\tRestar\n");
                printf("Introduzca los numeros a restar separados por comas\n");
                scanf("%d,%d", &uno, &dos);
                printf("%d - %d = %d\n", uno, dos, (uno - dos));
                break;
            case 3:
                printf("\tMultiplicar\n");
                printf("Introduzca los numeros a multiplicar separados por comas\n");
                scanf("%d,%d", &uno, &dos);
                printf("%d * %d = %d\n", uno, dos, (uno * dos));
                break;
            case 4:
                printf("\tDividir\n");
                printf("Introduzca los numeros a Dividir separados por comas\n");
                scanf("%d,%d", &uno, &dos);
                printf("%d / %d = %.2lf\n", uno, dos, ((double)uno / dos));
                break;
            case 5:
                printf("\tSalir\n");
                break; 
            default:
                printf("\tOpcion invalida.\n");
                break; 
        }
    } while (op != 5);
    return 0;
}
