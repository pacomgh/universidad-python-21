#Se debe ingresar el nombre del libro, su id, precio(flotante) y si tiene envio gratuito

nombreLibro = input("Ingresa el nombre del libro: ")
idLibro = int(input("Ingresa el id del libro: "))
precioLibro = float(input("Ingresa el precio del libro: "))
#se puede leer un string
envio = int(input("Tiene envío gratis?: \n 1)si \n 2)no \n"))
envioGratis = False

if envio == 1:
    envioGratis = True
elif envio == 2: 
    envioGratis = False
else:
    print("No has introducido un valor correcto para el envío gratuito")

print(f'''
    Nombre: {nombreLibro}
    Id: {idLibro}
    Precio: {precioLibro}
    Envio Gratis: {envioGratis}    
''')
