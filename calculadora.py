numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "Error: División por cero"
print(f"La suma de {numero1} + {numero2} es: {suma}")
print(f"La resta de {numero1} - {numero2} es: {resta}")
print(f"La multiplicación de {numero1} * {numero2} es: {multiplicacion}")
print(f"La división de {numero1} / {numero2} es: {division}")