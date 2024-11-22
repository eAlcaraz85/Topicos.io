import flet as ft

def main(page):
    page.title = "Hello, Flet!"
    page.add(ft.Text("Hello, World!"))

ft.app(target=main)
