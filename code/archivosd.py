import cv2
import numpy as np
import json
import os

# Funciones para manejar el registro de objetos detectados
def alta_objeto(color, tamano, area):
    nuevo_objeto = {"color": color, "tamano": tamano, "area": area}
    
    # Si el archivo existe, leer los datos existentes, sino crear uno nuevo
    try:
        if os.path.exists("detected_objects.json"):
            with open("detected_objects.json", "r") as file:
                datos = json.load(file)
        else:
            datos = []

        # Agregar el nuevo objeto detectado
        datos.append(nuevo_objeto)

        # Guardar los datos actualizados
        with open("detected_objects.json", "w") as file:
            json.dump(datos, file, indent=4)
        print("Nuevo objeto registrado.")
    except Exception as e:
        print(f"Error al registrar el objeto: {e}")

def consultar_objetos():
    try:
        with open("detected_objects.json", "r") as file:
            datos = json.load(file)
            if datos:
                for i, objeto in enumerate(datos):
                    print(f"Objeto {i}: Color={objeto['color']}, Tamaño={objeto['tamano']}, Área={objeto['area']}")
            else:
                print("No hay objetos registrados.")
    except FileNotFoundError:
        print("No se encontró el archivo de objetos detectados.")
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")

# Iniciar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Definir el rango de color que quieres rastrear en el espacio de color HSV (en este caso, azul)
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

img2 = None
i = 0

while True:
    # Capturar frame por frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir el frame de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Crear una máscara que detecte solo el color azul
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Filtrar la máscara con operaciones morfológicas
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Encontrar contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Si se encuentra al menos un contorno, seguir el objeto
    if contours:
        # Tomar el contorno más grande
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Encontrar el centro del contorno usando un círculo mínimo que lo rodee
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
        
        # Dibujar el círculo y el centro en el frame original si el radio es mayor que un umbral
        if radius > 10:
            i = i + 1
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 255), -1)
            cv2.rectangle(frame, (int(x-radius), int(y-radius)), (int(x+radius), int(y+radius)), (0, 0, 255), 3)
            img2 = frame[int(y-radius):int(y+radius), int(x-radius):int(x+radius)]
            cv2.imshow('img2', img2)
            
            # Calcular el área del objeto detectado
            area = cv2.contourArea(largest_contour)
            
            # Registrar el objeto detectado (alta)
            alta_objeto("azul", radius, area)
    
    # Mostrar el frame
    cv2.imshow('Frame', frame)
    
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Consultar los objetos detectados
#consultar_objetos()

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
