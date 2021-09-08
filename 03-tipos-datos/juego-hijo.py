vacaciones = False
diaDescanso = False

val1 = int(input(("Hoy es dia de descanso? 1)Si 2)No \n")))
val2 = int(input(("Son vacaciones? 1)Si 2)No \n")))

if val1 == 1:
    vacaciones = True
else:
    vacaciones = False

if val2 == 1:
    diaDescanso = True
else:
    diaDescanso = False
    

print("Usando or para hacer las comparaciones")
#esta expresion se evalua como la parte positiva
if vacaciones or diaDescanso:
    print("Puede asistir al juego de su hijo")
else:#esta expresion se evalua como la parte negativa
    print("Tiene deberes, no puede asistir al juego de su hijo")

print("Usando not para hacer las comparaciones")
#Esta expresion se evalua ahora como la parte negativa
if not (vacaciones or diaDescanso):
    print("Tiene deberes, no puede asistir al juego de su hijo")
else:#esta expresion se evalua ahora como la parte positiva
    print("Puede asistir al juego de su hijo")
