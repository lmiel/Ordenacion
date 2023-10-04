
"""
SOLUCION UTILIZANDO .SORT()

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
    t -= 1"""

def binay_search(arr, start, end, n):
    mid = int((start + end) / 2)
    if start >= end:
        return mid is False
    elif arr[mid] < n:
        return binay_search(arr, mid + 1, end, n)
    elif arr[mid] > n:
        return binay_search(arr, start, mid, n)
    else:
        while arr[mid] == n and mid != 0:
            mid -= 1
        return (mid + 1, True)

def binary_search_insert(arr, n):
    pos, exists = binay_search(arr, 0, len(arr), n)
    if not exists:
        arr.insert(pos, n)

for x in range(int(input())):
    student_count = 0
    input()
    line = list
    students = []
    for student in line:
        binary_search_insert(students, student)
    print(len(students))
