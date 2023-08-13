# Sistema de Log para pipelines de dados em Python

Este projeto implementa um sistema de log para pipeline de dados em Python. Permitindo que informações sobre sua execução, bem como quaisquer erros, possam ser salvas para análise futura após execução.

## Funcionalidades

1. **Configuração do Logger:** Define a configuração padrão para o logger, incluindo o formato das mensagens e os manipuladores.
2. **Filtro Personalizado:** Um filtro que previne a logagem de mensagens que começam com a palavra "senha".
3. **Decorador de Logging:** Um decorador que pode ser aplicado a qualquer função para logar informações ao iniciar e concluir a execução da função. Também loga erros automaticamente se ocorrerem durante a execução.
4. **Função de Divisão:** Um exemplo de função que utiliza o decorador de logging.

## Instalação e Execução com Poetry

Poetry é uma ferramenta para gerenciamento de dependências e empacotamento em Python.

### Pré-requisitos

* Certifique-se de ter o [Poetry](https://python-poetry.org/docs/#installation) instalado.

### Como usar

1. Clone este repositório:
    
    ```bash
    git clone [link-do-seu-repositório]
    ```
    
2. Navegue até o diretório do projeto:
    
    ```bash
    cd [nome-do-diretório-do-projeto]
    ```
    
3. Instale as dependências do projeto com o Poetry:
    
    ```
    poetry install
    ```
    
    Esta etapa irá criar um ambiente virtual e instalar todas as dependências especificadas no `pyproject.toml`.
    
4. Ative o ambiente virtual do Poetry:
    
    ```
    poetry shell
    ```
    
5. Execute o arquivo `main.py` para ver o sistema de logging em ação:
    
    ```css
    python main.py
    ```
    