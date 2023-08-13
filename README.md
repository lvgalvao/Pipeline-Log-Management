# Sistema de Logging para Pipelines em Python

Este projeto implementa um sistema de logging para pipelines de dados em Python. Ele permite que informações sobre sua execução, bem como quaisquer erros que ocorram, sejam salvas de forma organizada e detalhada.

## Estrutura de Diretório

```lua
Pipeline-Log-Management/
|-- main.py
|-- .env
|-- service/
|   |-- __init__.py
|   |-- transformation.py
|
|-- utility/
|   |-- __init__.py
|   |-- logger_standard/
|   |   |-- __init__.py
|   |   |-- logger_config.py
|   |   |-- logger_decorator.py
|   |
|   |-- logger_loguru/
|   |   |-- __init__.py
|   |   |-- logger_config.py
|   |   |-- logger_decorator.py
|   |
|   |-- logger_sentry/
|   |   |-- __init__.py
|   |   |-- logger_config.py
|   |   |-- logger_decorator.py
|
|-- logs/
|   |-- (Arquivos de logs gerados)
|
```

## Configurações

* **SENTRY**: Se você pretende utilizar o logger do Sentry, insira seu DSN no arquivo `.env` da seguinte forma:
    
    ```makefile
    DSN=seu_dsn_aqui
    ```
    
    Certifique-se de não compartilhar seu DSN publicamente.
    
* **Mudança de Logger**: Para utilizar diferentes loggers, você deverá alterar as importações e configurações nos arquivos `main.py` e `service/transformation.py`. Os arquivos de configuração dos loggers estão localizados na pasta `utility`.
    

## Como usar

1. Clone este repositório.
2. Configure o arquivo `.env` com as variáveis de ambiente necessárias.
3. Certifique-se de ter todas as dependências instaladas.
4. Execute o arquivo `main.py` para ver o sistema de logging em ação.