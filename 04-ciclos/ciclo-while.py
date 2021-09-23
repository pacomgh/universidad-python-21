#uso del ciclo while
contador = 0

while contador < 3:
    print(contador)
    contador+=1
else:
    print("Fin ciclo while")

#uso del ciclo for
cadena = 'Holanda'

for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")

#uso del break
#este ejercicios va a terminar cuando termine la primera letra a
for letra in cadena:
    if letra == 'a':
        print(f'caracter encontrado {letra}')
        break#el break nos saca del ciclo sin pasar al else
else:
    print('fin del ciclo for')
