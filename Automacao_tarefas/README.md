# Automação de Cadastro de Produtos

Este projeto utiliza Python e a biblioteca PyAutoGUI para automatizar o processo de cadastro de produtos em um sistema online. Ele lê uma lista de produtos de um arquivo CSV e preenche os campos necessários no sistema, realizando o login e o cadastro de forma automática.

## Recursos

- Login automático em um sistema web
- Importação de dados de produtos a partir de um arquivo CSV
- Cadastro automático de produtos no sistema
- Manipulação do mouse e teclado usando PyAutoGUI

## Estrutura do Projeto

1. **Importação das bibliotecas necessárias**
2. **Abertura do navegador e acesso ao sistema**
3. **Login no sistema**
4. **Importação da base de produtos**
5. **Cadastro de produtos**
6. **Repetição do processo até o final da lista**

## Tecnologias Utilizadas

- Python
- PyAutoGUI
- Pandas

## Pré-requisitos

Antes de executar o projeto, você precisa instalar as bibliotecas necessárias:

```bash
pip install pyautogui pandas
```

### Observação

- O PyAutoGUI pode não funcionar corretamente em alguns ambientes (como servidores sem interface gráfica). Certifique-se de executar o script em um ambiente com interface gráfica.

## Como Começar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/automacao-cadastro-produtos.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd automacao-cadastro-produtos
   ```

3. Prepare sua base de dados de produtos:
   - Crie um arquivo `produtos.csv` com as colunas `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, e `obs` (observações).

4. Execute o script Python:

   ```bash
   python main.py
   ```

### Instruções de Uso

- O script abrirá o navegador e fará login no sistema da empresa.
- A partir daí, ele lerá o arquivo `produtos.csv` e iniciará o cadastro de cada produto automaticamente.
- Certifique-se de que a posição do cursor do mouse esteja nas áreas corretas antes de executar o script, pois ele depende de coordenadas fixas para clicar em campos.

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um fork do repositório e enviar um pull request. Sugestões e melhorias são sempre bem-vindas!

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- Agradecimentos especiais à comunidade de desenvolvimento Python e à documentação do PyAutoGUI.

---

Sinta-se à vontade para personalizar este README conforme necessário!