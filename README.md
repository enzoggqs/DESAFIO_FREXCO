## Django Crud

![Author](https://img.shields.io/badge/author-enzoggqs-blueviolet)

<h4 align="center">
  Repositório destinado a página criada para um CRUD feito com Django. Na aplicação temos 2 tabelas, as Regiões e as Frutas. As regiões podem ser cadastradas e modificadas de qualquer maneira, já as frutas devem ser assossiadas a uma região. A partir dessass informações o usuário pode manipular as regiões e frutas conforme ele quiser, desde que siga as regras citadas acima.
</h4>

<div align="center">
    <img src="./mysite/assets/root.png" alt="API Root">
    <img src="./mysite/assets/regions.png" alt="Regions">
    <img src="./mysite/assets/deleting-editing-region.png" alt="Edit Region">
    <img src="./mysite/assets/fruits.png" alt="Fruits">
    <img src="./mysite/assets/deleting-editing-fruit.png" alt="Edit Fruit">
</div>

## Tecnologias

No desenvolvimento do projeto, foi utilizado a linguagem [Python](https://www.python.org/) associada aos frameworks [Django](https://www.djangoproject.com/) e [Django Rest Framework](https://www.django-rest-framework.org/).

## Rodando a aplicação

- Para rodar o projeto, você precisa ter o [Python3](https://www.python.org/downloads/) instalado, de preferência com versões mais recentes.

**Clone o repositório e acesse a pasta clonada**

$ git clone https://github.com/enzoggqs/django_crud && cd django_crud

```
# Ative o ambiente virtual
$ cd vend && cd Scripts && ./activate

# Volte para a pasta raíz
$ cd .. && cd ..

# Acesse o projeto criado e rode o servidor
$ cd mysite & python manage.py runserver

```

A aplicação estará disponível para ser acessada em seu navegador em `http://localhost:8000` e estará pronta para interação com o usuário.

Made with 💜 by Enzo Gabriel [Check out my LinkedIn](https://www.linkedin.com/in/enzoggqs)
