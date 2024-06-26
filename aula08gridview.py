import flet as ft
import os

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page:ft.Page):
    gridview  = ft.GridView(expand=True,max_extent=150,child_aspect_ratio=1)
    page.add(gridview)

    for i in range(100):
        gridview.controls.append(ft.Container(ft.Text(f"Item {i}"),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.AMBER_700,
        border=ft.border.all(4, ft.colors.AMBER_900),
        border_radius=ft.border_radius.all(9)))


    page.update()
    
ft.app(target=main)