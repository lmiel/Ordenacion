
n = int(input()) # Cantidad de peliculas

films = []
for film in range(n):
    (start, end) = map(int, input().split())
    films.append([start, end])
    
films.sort(key=lambda x: x[1])
#Aqui ordenariamos las peliculas con otro algoritmo q no me da tiempo a hacer
sol = 1

b = films[0][1]
for film in films:
    if b <= film[0]:
        b = film[1]
        sol += 1

print(sol)