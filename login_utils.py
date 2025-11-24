import csv
import os
import flet as ft 


def verificar_login(login, senha):
    """
    verificar se o login e senha existem no CSV
    """
    if not os.path.exists(r"Relatorios\dados.csv"):
        return False
    
    try:
        with open(r"Relatorios\dados.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if len(linha) >= 2:
                    if linha[0] == login and linha[1] == senha:
                        return True
        return False
    except:
        return False
    
def mostrar_tela_sucesso(page, usuario):
    """
    Mostra tela quando o login é bem-sucedido
    """
    page.clean()

    # Logo (subtitua pela sua)
    logo = ft.Container(
        content=ft.Text("LOGO", size=30, color="White"),
        width=150,
        height=150,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE_700
    )

    page.add(
        logo,
        ft.Text(f"Bem vindo {usuario}!", size=30, color="white"),
        ft.Text("login realizado com sucesso!", color="green")
    )