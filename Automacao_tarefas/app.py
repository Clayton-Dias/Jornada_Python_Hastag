import time  # Importa o módulo time, que fornece funções para manipulação de tempo.
import pyautogui # Importa o módulo pyautogui, que permite controlar o mouse e o teclado. (instalação: pip install pyautogui)
import pandas as pd  # Importa o módulo pandas, usado para manipulação de dados em tabelas. (instalação: pip install pandas)

# Passo a passo do projeto:
    # 1: Entrar no sistema da empresa 
    # 2: Fazer login
    # 3: Importar a base de produtos pra cadastrar
    # 4: Cadastrar um produto
    # 5: Repetir o processo de cadastro até o fim


# Passo 1: Entrar no sistema da empresa 
    # nesse caso  https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Funções do pyautogui que serão utilizadas:
# pyautogui.write => escreve um texto no campo ativo.
# pyautogui.click => clica na posição atual do mouse.
# pyautogui.press => simula o pressionamento de uma tecla.
# pyautogui.hotkey => simula o pressionamento de um atalho de teclado (como Ctrl+C).

pyautogui.PAUSE = 0.5 # Define uma pausa de 0.5 segundos entre os comandos do pyautogui.

# Abrir o navegador
pyautogui.press("win")  # Pressiona a tecla do Windows para abrir o menu iniciar.
pyautogui.write("chrome")  # Escreve "chrome" para buscar o navegador Google Chrome.
pyautogui.press("enter")  # Pressiona Enter para abrir o Chrome.


# Passo 2: Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  # Escreve a URL do sistema no navegador.
pyautogui.press("enter")  # Pressiona Enter para acessar a URL.

time.sleep(3)  # Pausa a execução por 3 segundos para garantir que a página carregue.

# Clica na caixa de entrada de e-mail, usando coordenadas (x=742, y=411).
pyautogui.click(x=742, y=411)
pyautogui.write("email@email.com")  # Escreve o e-mail no campo apropriado.

# Passa para o próximo campo (senha) pressionando a tecla Tab.
pyautogui.press("tab")
pyautogui.write("Eume@mo")  # Escreve a senha no campo de senha.

# Aperta o botão de login, clicando em uma posição específica na tela.
pyautogui.click(x=957, y=569)
# ou pyautogui.press("tab") e pyautogui.press("enter")

time.sleep(3)  # Pausa novamente para permitir que o login seja processado.


# Passo 3: Importar a base de produtos pra cadastrar
# importar pandas

tabela = pd.read_csv("produtos.csv")  # Lê a base de dados de produtos a partir de um arquivo CSV.
#print(tabela)  # Imprime a tabela no console (comentada).


# Passo 4: Cadastrar um produto

for linha in tabela.index: # Itera sobre cada linha da tabela de produtos.

    # texto = string = str()

    # Código do Produto
    pyautogui.click(x=743, y=295)  # Clica no campo do código de produto.
    codigo = tabela.loc[linha, "codigo"]  # Obtém o código do produto da tabela.
    pyautogui.write(str(codigo))  # Escreve o código no campo.

    # Marca do Produto
    marca = tabela.loc[linha, "marca"]  # Obtém a marca do produto da tabela.
    pyautogui.press("tab")  # Passa para o próximo campo.
    pyautogui.write(str(marca))  # Escreve a marca no campo.

    # Tipo do Produto
    tipo = tabela.loc[linha, "tipo"]  # Obtém o tipo do produto da tabela.
    pyautogui.press("tab")  # Passa para o próximo campo.
    pyautogui.write(str(tipo))  # Escreve o tipo no campo.

    # Categoria do Produto
    categoria = tabela.loc[linha, "categoria"]  # Obtém a categoria do produto da tabela.
    pyautogui.press("tab")  # Passa para o próximo campo.
    pyautogui.write(str(categoria))  # Escreve a categoria no campo.

    # Preço Unitário do Produto
    preco_unitario = tabela.loc[linha, "preco_unitario"]  # Obtém o preço unitário do produto da tabela.
    pyautogui.press("tab")  # Passa para o próximo campo.
    pyautogui.write(str(preco_unitario))  # Escreve o preço no campo.

    # Custo do Produto
    custo = tabela.loc[linha, "custo"]  # Obtém o custo do produto da tabela.
    pyautogui.press("tab")  # Passa para o próximo campo.
    pyautogui.write(str(custo))  # Escreve o custo no campo.

    # OBS (Observações)
    obs = tabela.loc[linha, "obs"]  # Obtém a observação do produto da tabela.
    pyautogui.press("tab")  # Passa para o próximo campo.
    pyautogui.write(str(obs))  # Escreve a observação no campo.

    if not pd.isna(obs):  # Verifica se a observação não é NaN (vazia).
        pyautogui.write(str(tabela.loc[linha, "obs"]))  # Escreve a observação, caso exista.

    # Enviar o formulário
    #pyautogui.click(x=869, y=953)  # (Comentado) Clicar em um botão para enviar o formulário.
    pyautogui.press("tab")  # Passa para o botão de enviar.
    pyautogui.press("enter")  # Pressiona Enter para enviar.

    # Rola a página para cima para preparar para o próximo cadastro.
    pyautogui.scroll(5000)  # Realiza um scroll para cima, facilitando o próximo cadastro.

    # Passo 5: Repetir o processo de cadastro até o fim
    # (Esse passo já está incorporado no loop que itera sobre os produtos da tabela)