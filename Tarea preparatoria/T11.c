#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int* eliminarDuplicados(const int* arr, int size, int* newSize) {
    int* result = (int*)malloc(size * sizeof(int));
    int resultSize = 0;

    if (!result) {
        *newSize = 0;
        return NULL;
    }

    // Copiar y ordenar la matriz
    int* sortedArr = (int*)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        sortedArr[i] = arr[i];
    }
    qsort((void*)sortedArr, size, sizeof(sortedArr[0]), compare);

    for (int i = 0; i < size; i++) {
        if (i == 0 || sortedArr[i] != sortedArr[i - 1]) {
            result[resultSize] = sortedArr[i];
            resultSize++;
        }
    }

    free(sortedArr);

    *newSize = resultSize;
    return result;
}

int main() {
    int input[] = {1, 3, 8, 8, 2, 3, 4, 1};
    int size = sizeof(input) / sizeof(input[0]);

    int newSize;
    int* result = eliminarDuplicados(input, size, &newSize);

    if (!result) {
        printf("Error allocating memory.\n");
        return 1;
    }

    printf("Original Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", input[i]);
    }

    printf("\nArray without Duplicates: ");
    for (int i = 0; i < newSize; i++) {
        printf("%d ", result[i]);
    }

    free(result);

    return 0;
}

