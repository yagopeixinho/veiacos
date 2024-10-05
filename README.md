<div align="center">
     <img src="https://github.com/yagopeixinho/veiacoPlataforma/raw/master/src/assets/logos/VeiacoDarkLogo.png">
</div>

<h4 align="center">Veiaco: porque gerenciar dívidas de amigos nunca foi tão fácil (ou menos constrangedor) </h4>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/yagopeixinho/veiacoBackend?color=58ADE2">
    <img src="https://img.shields.io/github/languages/count/yagopeixinho/veiacoBackend?color=E390D2">
    <img src="https://img.shields.io/github/license/yagopeixinho/veiacoBackend?color=fecf10">
</p>

Restful API para o projeto Veiaco - [veiaco](https://github.com/yagopeixinho/veiacoPlataforma)
> Esse é o *back-end* do projeto Veiaco! Cheque [veiacoPlataforma](https://github.com/yagopeixinho/veiacoPlataforma) para mais informação

<br/>

## Instalação &nbsp; [![pyVersion310](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/download/releases/3.10/)

Antes de rodar o front-end projeto, é necessário ter instalado em sua máquina:

- [Git](https://git-scm.com/)
- MySQL

### Clonando repositório

```bash
$ git clone git@github.com:yagopeixinho/veiacoBackend.git
```

### Ambiente Virtual

- No diretório do projeto que foi clonado, crie um ambiente virtual

```bash
$ python3 -m venv venv
# Esse comando vai criar um ambiente virtual

$ source venv/bin/activate
# Esse comando vai ativar o ambiente virtual que foi criado anteriormente
```

- Instale as dependências utilizando o pip
```bash
$ pip3 install -r requirements.txt
# Isso vai instalar todas as dependências para rodar o projeto
```

### Variáveis de Ambiente

- Para iniciarmos o projeto precisamos declarar algumas variáveis de ambiente responsáveis pela definição de informações importantes, como o ponto de entrada do APP e SECRET_KEY

```bash
# No diretório do projeto crie o arquivo responsável pela definição das variáveis de ambiente
$ touch .env
```

- Dentro do arquivo `.env` cole as variáveis de ambiente mínimas para rodar o projeto

```bash
# Para encriptar as senhas dos usuários
SECRET_KEY="escolhaUmaSenhaSegura"

# Ponto de entrada para rodar o APP
FLASK_APP="veiaco.py"
```

### Banco de Dados

- Dentro do CLI do MySQL, crie o banco de dados localmente

```Mysql
mysql> CREATE DATABASE veiaco;
```

- O Banco de Dados foi criado, porém ainda não possui nenhuma tabela ou informação. Esse é o trabalho do Flask-Migrate. Dentro do back-end:

```bash
$ flask db upgrade
```



