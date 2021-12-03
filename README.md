<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/dvduardo/trabalhos-sd">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/dvduardo/trabalhos-sd">
  <a href="https://www.linkedin.com/in/dvduardo/">
    <img alt="Feito pela David" src="https://img.shields.io/badge/feito%20por-David-%237519C1">
  </a>

# SISTEMAS DISTRIBUIDOS
Serão adicionados nesse repositorio todos os trabalhos solicitados na materia de Sistemas Distribuidos
  
### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina o [PYTHON](https://www.python.org/downloads)

# Ping-pong(cliente-servidor)
No primeiro projeto desenvolvido temos a comunicação atraves de um socket simples entre um servidor e um cliente. Basicamente os dois se conectam e conversam até um dos participantes mandar a mensagem SAIR, a qual fecha a comunicação entre ambos.

  
  ## 🚀 Como executar o projeto
  
  
  1. Extraia o projeto para sua maquina.
2. Dentro da pasta, abra dois prompts de comando (CMD) e digite em cada um o seguinte comando e clique ENTER:`python cliente.py` e `python servidor.py`
  ![image](https://user-images.githubusercontent.com/12902233/144547982-f3fdf3d9-d633-441c-bb76-c0d8629e5e29.png)
  2.1. IMPORTANTE : Sempre inicie primeiramente o SERVIDOR.
3. Para cancelar o processo, envie a mensagem `SAIR` a partir do SERVIDOR:
  ![image](https://user-images.githubusercontent.com/12902233/144548884-6d9ef8ed-c27d-4912-8391-6874c6d3ad82.png)
  ![image](https://user-images.githubusercontent.com/12902233/144549458-8f36261d-3e09-4e13-99c9-f85c9a2c65ce.png)
  
4. Se mandar a mensagem `SAIR` a partir do CLIENTE, apenas ele sera fechado, o SERVIDOR ficara a espera de um novo cliente se conectar:
  ![image](https://user-images.githubusercontent.com/12902233/144549725-1904bc0a-b5f5-48d5-ab38-604db7d25c8e.png)
---







