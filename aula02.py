import flet as ft

def main(page:ft.Page):
    entrada_nome = ft.TextField(label="Digite seu login")
    entrada_senha = ft.TextField(label="Digite a sua senha")

    def salvar(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor, preencha os campos."
            page.update()
        if not entrada_senha.value  :
            entrada_senha.error_text = "Por favor, preencha os campos."
            page.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome} \nSenha: {senha}")
            page.clean()
            page.add(ft.Text(f"Olá, {nome}\n Seja bem vindo."))

    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Clique em min", on_click=salvar)
    )
    pass
  

ft.app(target=main)