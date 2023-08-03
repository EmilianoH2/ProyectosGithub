#include <stdio.h>

// Función para calcular el factorial de un número
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num;

    printf("Ingrese un número: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("El factorial no está definido para números negativos.\n");
    } else {
        int result = factorial(num);
        printf("El factorial de %d es %d.\n", num, result);
    }

    return 0;
}
