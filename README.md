
# ApiRestfulCrud

 Experiência com um crud usando flask e suas ferramentas


- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## Como rodar esse projeto

```sh
linux
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
WINDOWS
SET FLASK_APP=app
SET FLASK_ENV=Development
SET FLASK_DEBUG=True
```

## Como rodar esse projeto
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```
## Como fazer as migrações
```sh
flask db init
flask db migrate
flask db upgrade

```