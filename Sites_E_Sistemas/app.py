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

# Função para enviar mensagens no chat
def enviar_mensagem(pagina, chat, campo_enviar_msg, nome_user):
    texto_campo_msg = campo_enviar_msg.value  # Obtém o texto da caixa de mensagem
    if texto_campo_msg.strip():  # Verifica se a mensagem não está vazia
        mensagem = f"{nome_user}: {texto_campo_msg}"  # Formata a mensagem
        pagina.pubsub.send_all(mensagem)  # Envia a mensagem para todos os participantes do chat
        campo_enviar_msg.value = ""  # Limpa a caixa de mensagem após o envio
        pagina.update()  # Atualiza a interface

# Função para lidar com a entrada do usuário no chat
def entrar_chat(pagina, popup, chat, linha_enviar, caixa_nome):
    popup.open = False  # Fecha o popup de entrada
    nome_usuario = caixa_nome.value  # Obtém o nome do usuário
    pagina.add(chat)  # Adiciona o container do chat à página
    pagina.add(linha_enviar)  # Adiciona a linha de envio de mensagens à página

    # Envia mensagem informando que o usuário entrou no chat
    mensagem = f"{nome_usuario} entrou no chat"
    pagina.pubsub.send_all(mensagem)  # Notifica todos os participantes sobre a nova entrada
    pagina.update()  # Atualiza a interface

# Função para abrir o popup de entrada
def abrir_popup(pagina, popup):
    pagina.dialog = popup  # Define o popup como o diálogo atual
    popup.open = True  # Abre o popup para o usuário
    pagina.update()  # Atualiza a interface

# Função principal do aplicativo
def main(pagina):
    # Título do chat
    titulo = ft.Text("Zapzap")

    # Container para o chat
    chat = ft.Column()

    # Campo para digitar a mensagem
    campo_enviar_msg = ft.TextField(
        label="Digite sua mensagem", 
        on_submit=lambda e: enviar_mensagem(pagina, chat, campo_enviar_msg, caixa_nome.value)  # Chama a função ao enviar
    )

    # Botão para enviar a mensagem 
    botao_enviar = ft.ElevatedButton(
        "Enviar", 
        on_click=lambda e: enviar_mensagem(pagina, chat, campo_enviar_msg, caixa_nome.value)  # Chama a função ao clicar
    )

    # Linha que contém o campo de mensagem e o botão
    linha_enviar = ft.Row([campo_enviar_msg, botao_enviar])

    # Criação do popup de entrada
    caixa_nome = ft.TextField(
        label="Digite seu nome", 
        on_submit=lambda e: entrar_chat(pagina, popup, chat, linha_enviar, caixa_nome)  # Chama a função ao enviar
    )
    botao_popup = ft.ElevatedButton(
        "Entrar no chat", 
        on_click=lambda e: entrar_chat(pagina, popup, chat, linha_enviar, caixa_nome)  # Chama a função ao clicar
    )
    popup = ft.AlertDialog(
        title=ft.Text("Bem vindo ao Zapzap"), 
        content=caixa_nome, 
        actions=[botao_popup]  # Adiciona o botão de entrada ao popup
    )

    # Botão para iniciar o chat
    botao = ft.ElevatedButton(
        "Iniciar chat", 
        tooltip="Clique aqui para começar o chat", 
        on_click=lambda e: abrir_popup(pagina, popup)  # Chama a função ao clicar
    )

    # Adiciona os elementos iniciais à página
    pagina.add(titulo)
    pagina.add(botao)

    # Assina o evento de recebimento de mensagens
    # Quando uma mensagem é recebida, ela é adicionada ao chat e a interface é atualizada
    pagina.pubsub.subscribe(lambda mensagem: chat.controls.append(ft.Text(mensagem)) or pagina.update())

# Executa a função principal com o Flet
#ft.app(main)
# Executa a função principal com o Flet, abrindo no navegador
ft.app(main, view=ft.AppView.WEB_BROWSER, port=8000)  # Use esta linha para abrir no navegador
