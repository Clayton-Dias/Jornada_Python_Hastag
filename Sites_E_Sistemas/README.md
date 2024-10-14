# Aplicativo de Chat Zapzap

Zapzap é um aplicativo de chat simples construído usando Flet. Ele permite que os usuários insiram seus nomes e conversem com outras pessoas em tempo real.

## Recursos

- Interface amigável
- Mensagens em tempo real
- Entrada de nome simples para identificação do usuário
- Design responsivo

## Como Começar

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Você também precisará instalar a biblioteca Flet.

```bash
pip install flet
```

### Executando o Aplicativo

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/zapzap.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd zapzap
   ```

3. Execute o aplicativo:

   ```bash
   python main.py
   ```

4. Abra seu navegador e acesse `http://localhost:8000` para começar a conversar!

## Visão Geral do Código

O aplicativo consiste em uma função principal que configura a interface do usuário e gerencia as interações. Os componentes principais incluem:

- **Título e Botão de Início**: Exibe o título do chat e um botão para iniciar a conversa.
- **Popup de Entrada do Usuário**: Solicita que o usuário insira seu nome antes de entrar no chat.
- **Área do Chat**: Exibe as mensagens enviadas pelos usuários.
- **Campo de Entrada de Mensagem**: Permite que os usuários escrevam e enviem mensagens.

### Funções Principais

- `enviar_mensagem(evento)`: Gerencia o envio de mensagens para o chat.
- `entrar_chat(evento)`: Controla a entrada do usuário no chat e atualiza a interface conforme necessário.
- `enviar_mensagem_tunel(mensagem)`: Atualiza o chat com novas mensagens.

## Contribuindo

Se você quiser contribuir para o Zapzap, sinta-se à vontade para fazer um fork do repositório e enviar um pull request. Melhorias ou sugestões são bem-vindas!

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- [Flet](https://flet.dev) - O framework usado para construir este aplicativo.

---

Sinta-se à vontade para modificar este README conforme necessário!