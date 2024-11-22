import flet as ft

# Función principal que define la interfaz de la app
def main(page: ft.Page):
    # Título de la ventana
    page.title = "Ejemplo básico de Flet"
    
    # Campo de texto donde el usuario puede escribir
    text_field = ft.TextField(label="Escribe algo aquí")
    
    # Label para mostrar el resultado
    result = ft.Text(value="")
    
    # Función que se ejecuta al hacer clic en el botón
    def button_clicked(e):
        result.value = f"Has escrito: {text_field.value}"  # Actualizar el texto
        page.update()  # Actualizar la página para mostrar los cambios
    
    # Botón que ejecuta la función cuando se hace clic
    button = ft.ElevatedButton(text="Mostrar texto", on_click=button_clicked)
    
    # Añadir los elementos a la página
    page.add(text_field, button, result)

# Ejecutar la app
ft.app(target=main)
