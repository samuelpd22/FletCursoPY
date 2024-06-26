from flet import *
#flet -r "nomeaplicação.py"
def main(page:Page):
    page.add(
        Text("Ola mundo!", size=20, color="white"),
        Container(
            width=200,
            height=200,
            bgcolor=colors.AMBER_100,
            border_radius=5
        ),
        Text("Texto 2 ", size=20, color="white"),
        TextField()
    )



app(target=main)