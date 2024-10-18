# Solicitar la edad del usuario
edad = int(input("Ingresa tu edad: "))

# Verificar la condición de la edad
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres mayor de edad.")
else:
    print("Eres una persona de la tercera edad.")
