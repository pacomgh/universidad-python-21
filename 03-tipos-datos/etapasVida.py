#0-10 infancia increible
#10-20 muchos cambios y mucho estudio
#20-30 amor y comienza el trabajo
#cualquier otr valor, etapa de la vida no reconocida

edad = int(input("Ingresa un valor numerico para la edad: "))

if edad >= 0 and edad < 10:
    print("La infancia es increible")
elif edad >= 10 and edad<20:
    print("Muchos cambios y mucho estudio")
elif edad>=20 and edad<30:
    print("Amor y el trabajo comienza")
else:
    print("Etapa de la vida no reconocida")
