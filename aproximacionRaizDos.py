"""a = 2 + (1/2)
b = 0

aproximacion = 1000
for i in range(aproximacion):
    b = 1 / a
    a = 2 + b


resultado = 1 + 1 / a

print(resultado)"""


a = [1, 2]
n = 2

#a += n igual a = a + n

aproximacion = int(input("¿Que numero de aproximacion quieres?: "))
for i in range(aproximacion - 1):
    a[0] += (n * a[1])

    a.reverse()
    print(a)

a[0] += (1 * a[1])

print(a)
print(a[0] / a[1])