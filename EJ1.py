
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
    