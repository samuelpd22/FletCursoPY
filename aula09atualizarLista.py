from flet import *

def main(page:Page):
    lv = ListView(expand=1,spacing=10,item_extent=50)
    page.add(lv)

    for linha in range(4000):
        lv.controls.append(Text(f"Linha {linha}"))

        #vai renderizar por partes
        if linha % 200 == 0:
            page.update()



    page.update()


app(target=main)