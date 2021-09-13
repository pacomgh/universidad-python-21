edad = int(input("Introduce tu edad: "))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

#if veintes or treintas:
#normalmente se hace la evaluacion dentro del if
if ( edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    #print("Dentro de rango de los (20's) o (30's)")
    if veintes:
        print('Dentro de los 20\'s')
    elif treintas:
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')
else:
    print("No esta dentro de los 20's ni de los 30's")

#print(veintes)
#print(treintas)
