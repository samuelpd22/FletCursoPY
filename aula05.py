import flet as ft


def main(page: ft.Page):
 
    lista = ft.ListView(spacing=2, expand=True)

    for linha in range(100):
        lista.controls.append(ft.Text(f"Estamos na linha {linha}"))
    
    page.add(lista)


ft.app(target=main)