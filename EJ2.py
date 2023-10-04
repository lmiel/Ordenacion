"""Hay n niños que quieren subir a una noria, y tu tarea es encontrar una góndola para cada
niño.
Cada góndola puede tener uno o dos niños, y además, el peso total en una góndola no
puede exceder x. Conoces el peso de cada niño.
¿Cuál es el número mínimo de góndolas necesarias para los niños?
"""

n, x = map(int, input().split())
#n niños
#x peso maximo por gondola

a = list(map(int, input().split()))
#

output = 0
a.sort()
i = 0
f = n-1

while i <= f:
    
    