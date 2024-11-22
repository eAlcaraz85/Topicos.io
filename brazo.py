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
        self.hombro.angulo_objetivo = posiciones_objetivo[0]
        self.codo.angulo_objetivo = posiciones_objetivo[1]
        self.muneca.angulo_objetivo = posiciones_objetivo[2]
        self.pinza.angulo_objetivo = posiciones_objetivo[3]

        self.hombro.actualizar_posicion()
        self.codo.actualizar_posicion()
        self.muneca.actualizar_posicion()
        self.pinza.actualizar_posicion()


def guardar_posiciones(self, nombre_archivo):
      with open(nombre_archivo, 'w') as archivo:
          archivo.write(f'Hombro: {self.hombro.angulo_actual}\n')
          archivo.write(f'Codo: {self.codo.angulo_actual}\n')
          archivo.write(f'Muñeca: {self.muneca.angulo_actual}\n')
          archivo.write(f'Pinza: {self.pinza.angulo_actual}\n')        

guardar_posiciones("ejemplo.txt")          
