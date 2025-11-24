import flet as ft
import csv
from login_utils import verificar_login, mostrar_tela_sucesso

def main(page:ft.Page): #Função que define como o nosso app irá se comportar 
    page.title = "Cadastro Login" # Título do nosso app
    page.theme_mode = "dark" # Tema que altera cor de fundo, botões e textos 
    page.vertical_alignment = "center" # centraliza na vertical
    page.horizontal_alignment = "center" #centraliza na horizontal
    page.window.center() # faz com que o flete inicialize no centro do monitor
    page.window.width = 600 # tamanho na horizontal
    page.window.height = 800 #tamanho na vertical

    def clique(e): # função para agir depois do clique em cadastro!!
        valor_login = texto_login.value # pegando valores digitados e guardando em variaveis
        valor_senha = texto_senha.value # pegando valores digitados e guardando em variaveis

        with open(r"Relatorios\dados.csv", "a",newline="") as arquivo: # salvando no csv
            escritor = csv.writer(arquivo)
            escritor.writerow([valor_login,valor_senha])

        page.open(ft.SnackBar(ft.Text(f"Conta cadrastada ! Bem vindo(a) {valor_login}", color="white"),bgcolor="green",duration=1.7))
        # aqui irá aparecer uma msg para o usuario informando o cadastro e dando boas vindas
        page.update()

        # entrar
    def entrar(e):
            login = texto_login.value
            senha = texto_senha.value

            if verificar_login(login, senha):
               mostrar_tela_sucesso(page, login)
            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text("login ou senha incorretos", color="White"),
                    bgcolor="red"
                )
                page.snack_bar.open = True
                page. update()


    titulo = ft.Text("Login", color="white" ,size=40) #titulo da página
    texto_login = ft.TextField(label="Login", # entrada de texto (senha)
                               focused_border_color="GREEN",
                               width=300,
                               autofocus=True
                               )
    texto_senha = ft.TextField(label="Senha",# Entranda de texto (senha)
                                focused_border_color="GREEN",
                                password=True, # Declarando o tipo de TextField
                                can_reveal_password=True, #revela a senha
                                width=300)
    
    botao_cadastro = ft.ElevatedButton("Cadastro",
                              on_click=clique,
                              width=100,
                              bgcolor="BLUE",
                              color="white")
    botao_entrar = ft.ElevatedButton("Entrar",
                              on_click=entrar,
                              width=100,
                              bgcolor="GREEN",
                              color="white")
    
    page.add(titulo,texto_login,texto_senha, # page.add é responsavel por mostrar na tela so usuario os itens
            ft.Row([botao_cadastro,botao_entrar],alignment="center")) # ft.Row é uma configuração aparte (linha), onde usamos para compor 1 ou ma
    
ft.app(target=main) # Deixa o flet em loop, para que não abra e feche
            