from io import open
import pickle
archivo = 'personas.txt'

fichero = open(archivo,"r",encoding='utf8')
lineas = fichero.readlines()
fichero.close()
del(fichero)

personas = []

for linea in lineas:
    linea = linea.replace("\n","")
    if len(linea) != 0:
        campos = linea.split(";")    
        persona =   {"id":campos[0], "nombre":campos[1], "apellidos":campos[2], "nacimiento":campos[3]}
        personas.append(persona)
        
for p in personas:
    output = "( id => {} ) {} {} => {} ".format(
            p['id'],
            p['nombre'],
            p['apellidos'],
            p['nacimiento']
        )
    print(output)


