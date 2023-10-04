"""Eres profesor de una clase de la que te piden que pases asistencia. Cada alumno, según
llega a clase, confirma su asistencia y en la lista aparece su número identificador como un
entero. Sin embargo, el sistema es algo nuevo y a ratos vuelve a aparecer por error en la
lista un alumno ya registrado.
Tu objetivo es, dada la lista de identificadores A con longitud n, obtener el número de
identificadores únicos en ella sin hacer uso de estructuras adicionales (sets, listas, etc)."""
t = int(input("Casos de prueba:"))

while t != 0:
    n = int(input("Numero de alumnos:"))
    a = list(map(int, input().split()))
    a.sort()
    output = n
    for i in range(n-1):
        if a[i] == a[i+1]:
            output -= 1
    print(output)
    t -= 1
    