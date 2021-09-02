mayorEdad = 18

edad = int(input('Ingresa tu edad: '))

if edad < mayorEdad:
    print(f'Tu edad es {edad} aún no eres mayor de edad')
else:
    print(f'Tu edad es {edad} tienes la mayoría de edad, puedes votar')