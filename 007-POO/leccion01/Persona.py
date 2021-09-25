class Persona:
    #metodo inicializador, similar al constructor
    #metodo especial po __ dounder
    def __init__(self, nombre, apellido, edad):#self referencia al objeto que se va a crear, referencia de ese mismo objeto
        #atributos de instancia
        #self.nombre = 'Paco'
        self.nombre = nombre#atributo de clase = parametro
        self.apellido = apellido
        self.edad = edad


persona1 = Persona('Paco', 'Guzman', 22)#cuando se crea la clase se llama el init

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto persona1 contiene nombre: {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} anios')


persona2 = Persona('Pedro', 'Perez', 19)
print(f'El objeto persona2 contiene nombre: {persona2.nombre} {persona2.apellido} y tiene {persona2.edad} anios')
