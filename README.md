# Projeto de Análise de Dados e Automação

Este repositório contém diversos scripts em Python que realizam análises de dados e automação de tarefas. Os projetos utilizam bibliotecas populares como Pandas e PyAutoGUI, abordando desde análise de cancelamentos até automação de cadastro de produtos.

## Índice

1. [Análise de Cancelamentos](#análise-de-cancelamentos)
2. [Automação de Cadastro de Produtos](#automação-de-cadastro-de-produtos)
3. [Modelo de Previsão de Crédito](#modelo-de-previsão-de-crédito)
4. [Chat Simples com Flet](#chat-simples-com-flet)

## Análise de Cancelamentos

O script `analise_cancelamentos.py` realiza as seguintes etapas:

1. **Importação da Base de Dados**: Lê a base de dados de cancelamentos a partir de um arquivo CSV.
2. **Visualização e Limpeza**: Analisa a estrutura dos dados, removendo colunas e linhas desnecessárias ou vazias.
3. **Análise de Cancelamentos**: Calcula e exibe a contagem e porcentagem de cancelamentos.
4. **Causas dos Cancelamentos**: Utiliza gráficos para analisar as causas dos cancelamentos e propõe soluções.
5. **Filtragem de Dados**: Aplica filtros para analisar o impacto de diferentes variáveis nos cancelamentos.

### Dependências

```bash
pip install pandas plotly
```

## Automação de Cadastro de Produtos

O script `automacao_cadastro.py` automatiza o processo de cadastro de produtos em um sistema. As etapas incluem:

1. **Login no Sistema**: Acessa o sistema utilizando as credenciais fornecidas.
2. **Importação de Dados**: Lê a base de dados de produtos a partir de um arquivo CSV.
3. **Cadastro dos Produtos**: Itera sobre os produtos e preenche os campos no sistema automaticamente.

### Dependências

```bash
pip install pandas pyautogui
```

## Modelo de Previsão de Crédito

O script `modelo_previsao_credito.py` cria um modelo de machine learning para prever scores de crédito. As etapas incluem:

1. **Importação e Preparação dos Dados**: Lê a base de dados e transforma variáveis categóricas em numéricas.
2. **Divisão de Dados**: Separa os dados em conjuntos de treino e teste.
3. **Treinamento de Modelos**: Treina dois modelos: uma árvore de decisão e KNN.
4. **Avaliação**: Calcula a acurácia dos modelos e realiza previsões em novos dados.

### Dependências

```bash
pip install pandas scikit-learn
```

## Chat Simples com Flet

O script `chat_simples.py` cria um chat básico utilizando a biblioteca Flet. As etapas incluem:

1. **Interface do Usuário**: Cria uma interface simples para interação do usuário.
2. **Gerenciamento de Mensagens**: Permite que os usuários enviem e recebam mensagens em tempo real.
3. **Abertura no Navegador**: Possibilita a visualização do chat em um navegador.

### Dependências

```bash
pip install flet
```

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio
   ```

2. Instale as dependências necessárias para cada script.

3. Execute o script desejado:
   ```bash
   python nome_do_script.py
   ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um Pull Request ou relatar problemas.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

