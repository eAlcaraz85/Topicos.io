import json
import os

class Articulacion:
    def __init__(self, angulo_actual, angulo_objetivo, velocidad, limite_min, limite_max):
        self.angulo_actual = angulo_actual
        self.angulo_objetivo = angulo_objetivo
        self.velocidad = velocidad
        self.limite_min = limite_min
        self.limite_max = limite_max

    def actualizar_posicion(self):
        if self.angulo_actual < self.angulo_objetivo:
            self.angulo_actual += self.velocidad
            if self.angulo_actual > self.angulo_objetivo:
                self.angulo_actual = self.angulo_objetivo
        elif self.angulo_actual > self.angulo_objetivo:
            self.angulo_actual -= self.velocidad
            if self.angulo_actual < self.angulo_objetivo:
                self.angulo_actual = self.angulo_objetivo

class BrazoRobotico:
    def __init__(self):
        self.hombro = Articulacion(0, 0, 1, -90, 90)
        self.codo = Articulacion(0, 0, 1, 0, 135)
        self.muneca = Articulacion(0, 0, 1, -90, 90)
        self.pinza = Articulacion(0, 0, 1, 0, 180)

    def mover_a_posicion(self, posiciones_objetivo):
        # Actualiza los ángulos objetivo para cada articulación
        self.hombro.angulo_objetivo = posiciones_objetivo[0]
        self.codo.angulo_objetivo = posiciones_objetivo[1]
        self.muneca.angulo_objetivo = posiciones_objetivo[2]
        self.pinza.angulo_objetivo = posiciones_objetivo[3]

        # Actualiza cada articulación
        self.hombro.actualizar_posicion()
        self.codo.actualizar_posicion()
        self.muneca.actualizar_posicion()
        self.pinza.actualizar_posicion()

    def obtener_posiciones(self):
        # Retorna las posiciones actuales de las articulaciones
        return {
            "hombro": self.hombro.angulo_actual,
            "codo": self.codo.angulo_actual,
            "muneca": self.muneca.angulo_actual,
            "pinza": self.pinza.angulo_actual
        }

class ManejoArchivos:
    def __init__(self, archivo):
        self.archivo = archivo
        # Crear archivo si no existe
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump([], f)

    def alta(self, datos):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Añadir nuevos datos
        registros.append(datos)
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def baja(self, indice):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Eliminar por índice
        if 0 <= indice < len(registros):
            registros.pop(indice)
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def modificar(self, indice, nuevos_datos):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        # Modificar el registro por índice
        if 0 <= indice < len(registros):
            registros[indice] = nuevos_datos
        # Guardar los cambios
        with open(self.archivo, 'w') as f:
            json.dump(registros, f, indent=4)

    def consultar(self):
        # Cargar los datos existentes
        with open(self.archivo, 'r') as f:
            registros = json.load(f)
        return registros

def mostrar_menu():
    print("\nMenú del Brazo Robótico:")
    print("1. Alta (Guardar nueva posición)")
    print("2. Baja (Eliminar una posición por índice)")
    print("3. Modificación (Modificar una posición por índice)")
    print("4. Consultas (Mostrar todas las posiciones guardadas)")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    brazo = BrazoRobotico()
    archivo = ManejoArchivos("articulaciones.json")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":  # Alta
            # Captura nuevas posiciones de las articulaciones
            try:
                pos_hombro = float(input("Ángulo del hombro: "))
                pos_codo = float(input("Ángulo del codo: "))
                pos_muneca = float(input("Ángulo de la muñeca: "))
                pos_pinza = float(input("Ángulo de la pinza: "))
                brazo.mover_a_posicion([pos_hombro, pos_codo, pos_muneca, pos_pinza])
                archivo.alta(brazo.obtener_posiciones())
                print("Posición guardada exitosamente.")
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        elif opcion == "2":  # Baja
            try:
                indice = int(input("Ingrese el índice de la posición que desea eliminar: "))
                archivo.baja(indice)
                print("Posición eliminada exitosamente.")
            except ValueError:
                print("Error: Ingrese un índice válido.")
            except IndexError:
                print("Error: Índice fuera de rango.")

        elif opcion == "3":  # Modificación
            try:
                indice = int(input("Ingrese el índice de la posición que desea modificar: "))
                pos_hombro = float(input("Nuevo ángulo del hombro: "))
                pos_codo = float(input("Nuevo ángulo del codo: "))
                pos_muneca = float(input("Nuevo ángulo de la muñeca: "))
                pos_pinza = float(input("Nuevo ángulo de la pinza: "))
                brazo.mover_a_posicion([pos_hombro, pos_codo, pos_muneca, pos_pinza])
                archivo.modificar(indice, brazo.obtener_posiciones())
                print("Posición modificada exitosamente.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            except IndexError:
                print("Error: Índice fuera de rango.")

        elif opcion == "4":  # Consultas
            posiciones = archivo.consultar()
            if posiciones:
                for i, pos in enumerate(posiciones):
                    print(f"Posición {i}: Hombro={pos['hombro']}, Codo={pos['codo']}, Muñeca={pos['muneca']}, Pinza={pos['pinza']}")
            else:
                print("No hay posiciones guardadas.")

        elif opcion == "5":  # Salir
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción del menú.")

if __name__ == "__main__":
    main()
