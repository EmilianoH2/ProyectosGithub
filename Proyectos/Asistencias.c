#include <stdio.h>
#include <string.h>

#define MAX_ALUMNOS 100

struct Alumno {
    char nombre[50];
    int asistencias;
};

int main() {
    struct Alumno alumnos[MAX_ALUMNOS];
    int num_alumnos = 0;

    // Leer datos de los alumnos desde un archivo
    FILE *archivo = fopen("asistencias.txt", "r");
    if (archivo != NULL) {
        while (fscanf(archivo, "%s %d", alumnos[num_alumnos].nombre, &alumnos[num_alumnos].asistencias) == 2) {
            num_alumnos++;
        }
        fclose(archivo);
    }

    // Registrar las asistencias de los alumnos
    char nombre[50];
    int asistencias;
    printf("Ingrese el nombre del alumno ('fin' para terminar): ");
    scanf("%s", nombre);
    while (strcmp(nombre, "fin") != 0 && num_alumnos < MAX_ALUMNOS) {
        printf("Ingrese el número de asistencias para %s: ", nombre);
        scanf("%d", &asistencias);

        strcpy(alumnos[num_alumnos].nombre, nombre);
        alumnos[num_alumnos].asistencias = asistencias;
        num_alumnos++;

        printf("Ingrese el nombre del alumno ('fin' para terminar): ");
        scanf("%s", nombre);
    }

    // Guardar los datos de los alumnos en el archivo
    archivo = fopen("asistencias.txt", "w");
    if (archivo != NULL) {
        for (int i = 0; i < num_alumnos; i++) {
            fprintf(archivo, "%s %d\n", alumnos[i].nombre, alumnos[i].asistencias);
        }
        fclose(archivo);
    }

    // Mostrar las asistencias registradas
    printf("\nAsistencias registradas:\n");
    for (int i = 0; i < num_alumnos; i++) {
        printf("%s: %d asistencias\n", alumnos[i].nombre, alumnos[i].asistencias);
    }

    return 0;
}
