"""Implemente un algoritmo, usando una función recursiva, que resuelva la
siguiente
sumatoria: K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + ... + n ∗ p
● El programa debe pedir al usuario que ingrese un número n, y un número P,
● Luego debe calcular el valor de K(n, p) usando una función recursiva,
● Debe imprimir el resultado de K(n, p)
"""

def sumatoria_K(n, p):
    if n == 1:
        return p
    return n*p + sumatoria_K(n-1, p) #aquí s ellama a la funcion y s ehace recursiva



n=int(input("Digite valor de n :"))
p=int(input("Digite el valor de p :"))
print(sumatoria_K(n,p)) #llamamos a la funcion y pasamos los datos que ingresamos...