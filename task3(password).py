import flet as ft
from random import *
from string import *

def main(page: ft.Page):
    def des(e):
        page.controls.pop()
        page.update()
        
    def button_clicked(e):
        passwd=''
        global pas
        pas=' '
        if low.value:
            passwd+=ascii_lowercase
        if upp.value:
            passwd+=ascii_uppercase
        if num.value:
            passwd+=digits
        if sym.value:
            passwd+=punctuation
        if passwd and n.value:
            for i in range(int(n.value)):
                pas+=choice(passwd)
            global mm
            mm=ft.Text("Your Password is: "+pas,size=20,bgcolor=ft.colors.CYAN_ACCENT_100,)
            page.add(ft.Row(controls=[ft.Text('     '),ft.Text('     '),mm,re]))           
            page.update()
        else:
            def cl(e):
                page.close(al)
                page.update()
            al=ft.AlertDialog(title=ft.Text("Kindly check your inputs..!",size=20),actions=[ft.TextButton("ok", on_click=cl)])
            page.dialog = al
            al.open = True
            page.update()
       
        

    page.bgcolor = ft.colors.ORANGE_100
    page.window.width=500
    page.window.height=500
    page.window.left = 200
    page.window.top = 100
    page.window.resizable=False
    page.add(
    ft.Row(controls=[ft.Text("PASSWORD GENERATOR",size=25,color="RED",italic=True),],alignment=ft.MainAxisAlignment.CENTER))
    n=ft.TextField(label="Enter Length of Password?")
    page.add(ft.Row(controls=[n]))
    page.add((ft.Text("Select The Chacraters to be included?",size=23)))
    t2=ft.Text()
    upp = ft.Checkbox(label="Allow Uppercase Alphabets", value=False)    
    low = ft.Checkbox(label="Allow Lowercase Alphabets", value=False)
    num = ft.Checkbox(label="Use Numbers", value=False)
    sym = ft.Checkbox(label="Use Special Symbols", value=False)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked,color='red')
    re=ft.IconButton(icon=ft.icons.RESTORE_PAGE,icon_color="blue400",icon_size=20,tooltip="reset",on_click=des)
    page.add(ft.Row(controls=[ft.Text("    "),ft.Column(controls=[upp,low,num,sym,b,t2],spacing=10)]))

ft.app(target=main)
