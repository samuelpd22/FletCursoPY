import flet as ft

def main(page: ft.Page):
    #titulo da pagina
    page.title = "Teste"
    #tema
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()



ft.app(target=main)