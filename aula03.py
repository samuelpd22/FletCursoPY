import flet as ft

def app(page:ft.Page):
    
    def tecla(e: ft.KeyboardEvent):
        page.add(
            ft.Text(f"Tecla pressionada: {e.key}, Shift: {e.shift}, Ctrl: {e.ctrl}, Alt:{e.alt}, Win: {e.meta}")
        )
    page.on_keyboard_event = tecla

    page.add(
        ft.Text("Pressione qualquer tecla ou uma combinação de teclas (CTRL, SHIFT, ALT, WIN) ",size=30)
    )


ft.app(target=app)