# Chat (Hashzap|| Zapzap )
# 1 - título : Hashzap || Zapzap
# 2 - botão: Iniciar Chat
# 2.1 - quando clicar no botão: abrir um pop-up/modal/alerta
# 2.1.1 - Título: Bem vindo ao Hashzap || Zapzap
# 2.1.2 - Caixa de texto: Escreva seu nome que aparecerar no chat
# 2.1.3 - Botão: entrar no chat
# 2.1.3.1 - Quando clicar no botão: fechar popup, sumir com o título e o botão Iniciar chat
# carregar :
# A) o chat,
# B) campo de enviar mensagem
# C) e o botão enviar
# C.1) quando clicar no botão enviar: envia a mensagem para o chat
# C.2) limpar a caixa de mensagem

import flet as ft


# criar uma função principal para rodar o aplicativo/site
def main(pagina):

    # título
    titulo = ft.Text("Zapzap")
    
    # Função para enviar mensagem ao chat
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update() 
    
    # Assina o evento de recebimento de mensagens
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    # Função para processar o envio de mensagens
    def enviar_mensagem(evento):
        nome_user = caixa_nome.value
        texto_campo_msg = campo_enviar_msg.value        
        mensagem = f"{nome_user}: {texto_campo_msg}"
        
        # Envia a mensagem para todos no chat
        pagina.pubsub.send_all(mensagem)
                
        # limpar a caixa de enviar mensagem
        campo_enviar_msg.value = ""        
        pagina.update() 
    
    
    # Campo para digitar a mensagem
    campo_enviar_msg = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)   
    
    # Botão para enviar a mensagem 
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    # Container para o chat
    chat = ft.Column()
    
    # Linha que contém o campo de mensagem e o botão
    linha_enviar = ft.Row([campo_enviar_msg, botao_enviar])
    
    # Função para lidar com a entrada no chat
    def entrar_chat(evento):
        # Fecha o popup de entrada
        popup.open = False
        
        # Remove o título e o botão inicial da página
        pagina.remove(titulo)
        pagina.remove(botao)
        
        # Adiciona o chat e o campo de envio à página
        pagina.add(chat)
        pagina.add(linha_enviar)
        
        # Envia mensagem informando que o usuário entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"        
        pagina.pubsub.send_all(mensagem)
        
        pagina.update()
        
        

    # Criação do popup de entrada
    titulo_popup = ft.Text("Bem vindo ao Zapzap")
    caixa_nome = ft.TextField(label="Digite seu nome", on_submit=entrar_chat)
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    # Definição do popup
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    # botão inicial / Função para abrir o popup
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Botão para iniciar o chat
    botao = ft.ElevatedButton("Iniciar chat", tooltip="Clique aqui para começar o chat", on_click=abrir_popup)

    # Adiciona os elementos iniciais à página
    pagina.add(titulo)
    pagina.add(botao)


# Executa a função principal com o Flet
ft.app(main)
#ft.app(target=main, view = ft.WEB_BROWSER, port=8000)
