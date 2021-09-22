valor = int(input("Ingresa un valor: "))
valorMinimo = 0
valorMaximo = 5

dentroDeRango = valor >= valorMinimo and valor <= valorMaximo
#forma 1
'''if valor >= 0 and valor<=5:
    print("El valor esta dentro del rango")
else:
    print("El valor esta fuera del rango")'''

if dentroDeRango:
    print("El valor esta dentro del rango")
else:
    print("El valor esta fuera del rango") 


