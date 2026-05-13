#usuario = {"Nombre": "Laura", "Edad": 20, "ciudad": "Colombia", "Email": "laura@gmail.com"}

#acceder valor
#print(usuario["Nombre"])

#modificar valor
#usuario["Edad"] = 25

#anadir un nuevo par
#usuario["Profesión"] = "ingeniera"

#eliminar un elemento
#del usuario["ciudad"]

#usar el metodo get() para evitar errores si la clave no existe
#email = usuario.get("email", "No proporcionado")


#ejemplo recorrido
#for clave, valor in usuario.items():
    #print(f"{clave}: {valor}")

personas = ["Nombre", "Edad", "ciudad", "Email"]
diccionario1 = {"Nombre": "Laura", "Edad": 20, "ciudad": "Colombia", "Email": "laura@gmail.com"}
diccionario2 = {"Nombre": "Luis", "Edad": 23, "ciudad": "EEUU", "Email": "Luis@gmail.com"}
diccionario3 = {"Nombre": "jeison", "Edad": 27, "ciudad": "Las vegas", "Email": "jeison@gmail.com"}
diccionario4 = {"Nombre": "hector", "Edad": 45, "ciudad": "argentina", "Email": "hector@gmail.com"}
diccionario5 = {"Nombre": "julian", "Edad": 25, "ciudad": "california", "Email": "julian@gmail.com"}

lista_diccionarios = [diccionario1, diccionario2, diccionario3, diccionario4, diccionario5]
#for d in lista_diccionarios:
    #for p in personas:
     #print(p + " : " + str(d[p]))
print("Que usuario esta en la posicion 1: " + str(lista_diccionarios[1]["Nombre"]))




