"""2. Implemente un programa para convertir un número decimal a hexadecimal
ejm. el número 8642 en forma hexadecimal es: 21C2
"""

def convertidor_Decimal_a_Hexadecimal(numero):
    #hacemos un diccionaro poniendo el valor a  cada numero y letra
  diccionario = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

  if (numero < 16):
    return diccionario[numero]

  return convertidor_Decimal_a_Hexadecimal(numero//16) + diccionario[numero%16] #aquí s ellama a la funcion y s ehace recursiva
  
print(convertidor_Decimal_a_Hexadecimal(3210)) #llamamos a la funcion y pasamos los datos que ingresamos...