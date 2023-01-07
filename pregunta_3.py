"""3. Convertir un Número Entero a Cualquier Base Numérica,
El programa debe pedir al usuario que ingrese un número n, y un número p,
"""

def convertidor_Decimal_baseRandom(numero, base):
  diccionario = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    #hacemos un diccionaro poniendo el valor a  cada numero y letra
  if (numero < base):
    return diccionario[numero]

  return convertidor_Decimal_baseRandom(numero//base, base) + diccionario[numero%base] #aquí s ellama a la funcion y s ehace recursiva



n=float(input("Digite el número entero a convertir... :"))
p=float(input("Digite a que base numerica quiere convertir... :"))
print(convertidor_Decimal_baseRandom(n,p)) #llamamos a la funcion y pasamos los datos que ingresamos...