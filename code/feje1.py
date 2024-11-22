import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Hola, Mundo"))

ft.app(target=main, view="web_browser")
