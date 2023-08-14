# Sistema de Logging para Pipelines em Python

Este projeto implementa um sistema de logging para pipelines de dados em Python. Ele permite que informações sobre sua execução, bem como quaisquer erros que ocorram, sejam salvas de forma organizada e detalhada.

## Requisitos

* Python 3.11.3
* Poetry
* Docker (Optional)

## Estrutura de Diretório

```lua
Pipeline-Log-Management/
|-- Dockerfile
|-- app/
|   |-- main.py
|   |-- .env
|   |-- service/
|   |   |-- __init__.py
|   |   |-- transformation.py
|
|   |-- utility/
|   |   |-- __init__.py
|   |   |-- logger_standard/
|   |   |   |-- __init__.py
|   |   |   |-- logger_config.py
|   |   |   |-- logger_decorator.py
|   |
|   |   |-- logger_loguru/
|   |   |   |-- __init__.py
|   |   |   |-- logger_config.py
|   |   |   |-- logger_decorator.py
|   |
|   |   |-- logger_sentry/
|   |   |   |-- __init__.py
|   |   |   |-- logger_config.py
|   |   |   |-- logger_decorator.py
|
|-- logs/
|   |-- (Generated log files)
```

## Configurações

* **SENTRY**: Se você pretende utilizar o logger do Sentry, insira seu DSN no arquivo `.env` da seguinte forma:
    
    ```makefile
    DSN=seu_dsn_aqui
    ```
    
    Certifique-se de não compartilhar seu DSN publicamente.
    
* **Mudança de Logger**: Para utilizar diferentes loggers, você deverá alterar as importações e configurações nos arquivos `main.py` e `service/transformation.py`. Os arquivos de configuração dos loggers estão localizados na pasta `utility`.
    

## Como usar

### Configuração e Execução Tradicional

1. Clone este repositório.
    
2. Configure o arquivo `.env` com as variáveis de ambiente necessárias.
    
3. Navegue até o diretório `app`:
    
    ```bash
    cd app
    ```
    
4. Instale as dependências:
    
    ```bash
    poetry install
    ```
    
5. Execute o arquivo `main.py` para ver o sistema de logging em ação:
    
    ```bash
    python main.py
    ```
    

### Configuração e Execução com Docker

Se preferir rodar o projeto dentro de um container Docker, siga estes passos:

1. Construa a imagem Docker a partir da raiz do projeto:
    
    ```bash
    docker build -t pipeline-log-management .
    ```
    
2. Execute o projeto dentro de um container Docker:
    
    ```bash
    docker run -e DNS=seu_dsn_aqui pipeline-log-management
    ```