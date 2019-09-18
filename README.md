# Primeiro, clone este repositório na sua máquina:

- git clone https://github.com/rhayanebarros/pet-sistema.git

# Instalação:

- Tenha o Python instalado na sua máquina
- Instale o pip : python -m pip install --upgrade pip setuptools wheel
- Instalar virtual env: pip install virtualenv
- Criar seu ambiente virtual rode: virtualenv venv (venv foi o nome que eu dei para o meu ambiente sempre gere com este nome)
- Para ativar o seu ambiente virtual rode: venv\Scripts\activate
- Antes de instalar o Django devemos garantir que temos instalada a última versão do pip, que é o software que usamos para instalar o Django: python -m pip install --upgrade pip
- O arquivo "requirements.txt" guarda as dependências que serão instaladas utilizando o pip install: execute pip install -r requirements.txt
- para verificar se o django foi instalado rode: python
- depois rode: import django, e depois rode: django.get_version()
- a versão tem que ser Django==2.2.5
- saia do ambiente python com: exit()
- Aplique as migrações do banco: python manage.py migrate

# Rodando o projeto:

- Para rodar o projeto: python manage.py runserver

# Build do projeto:

# Referência:

- https://petshopcontrol.com.br/

# Git, branch(s) e git-flow:

- Neste projeto vamos usar um git-flow simplificado. Criei as branch(s): **master**, **stage** e **develop**.

- Todo o desenvolvimento deve ser feito na branch **develop**. Quando o código estiver pronto para ser homologado, é feito o merge da branch develop na **stage**. Uma vez homologado por todos e pronto para ser entregue ao cliente, é feito o merge da branch stage na **master**.

- Caso alguém encontre um bug em homologação, o desenvolvedor responsável faz a correção em **develop** e faz um novo merge em **stage**.

# Observações gerais:
