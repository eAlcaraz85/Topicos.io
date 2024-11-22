   import json

   # Función para realizar el alta de un nuevo registro
   def alta_usuario(nombre, edad):
       nuevo_registro = {"nombre": nombre, "edad": edad}
       try:
           with open("usuarios.json", "r+") as file:
               datos = json.load(file)
               datos.append(nuevo_registro)
               file.seek(0)
               json.dump(datos, file, indent=4)
           print(f"Usuario {nombre} agregado exitosamente.")
       except FileNotFoundError:
           with open("usuarios.json", "w") as file:
               json.dump([nuevo_registro], file, indent=4)
           print(f"Archivo creado y usuario {nombre} agregado exitosamente.")

   alta_usuario("Juan", 28)

   import json

   # Función para eliminar un registro basado en el índice
   def baja_usuario(indice):
       try:
           with open("usuarios.json", "r+") as file:
               datos = json.load(file)
               if 0 <= indice < len(datos):
                   usuario_eliminado = datos.pop(indice)
                   file.seek(0)
                   json.dump(datos, file, indent=4)
                   file.truncate()
                   print(f"Usuario {usuario_eliminado['nombre']} eliminado exitosamente.")
               else:
                   print("Índice fuera de rango.")
       except FileNotFoundError:
           print("No se encontró el archivo de usuarios.")

   baja_usuario(0)

   import json

   # Función para modificar un registro en base a su índice
   def modificar_usuario(indice, nuevo_nombre, nueva_edad):
       try:
           with open("usuarios.json", "r+") as file:
               datos = json.load(file)
               if 0 <= indice < len(datos):
                   datos[indice]["nombre"] = nuevo_nombre
                   datos[indice]["edad"] = nueva_edad
                   file.seek(0)
                   json.dump(datos, file, indent=4)
                   file.truncate()
                   print(f"Usuario en el índice {indice} modificado exitosamente.")
               else:
                   print("Índice fuera de rango.")
       except FileNotFoundError:
           print("No se encontró el archivo de usuarios.")

   modificar_usuario(0, "Ana", 30)

   import json

   # Función para consultar y mostrar todos los registros
   def consultar_usuarios():
       try:
           with open("usuarios.json", "r") as file:
               datos = json.load(file)
               if datos:
                   for i, usuario in enumerate(datos):
                       print(f"Usuario {i}: {usuario['nombre']}, Edad: {usuario['edad']}")
               else:
                   print("No hay usuarios registrados.")
       except FileNotFoundError:
           print("No se encontró el archivo de usuarios.")

   consultar_usuarios()
