# Como rodar

## Setup de desenvolvimento do projeto
### 1. Instalar bibliotecas
```sh
sudo apt install make python3-pip python3 docker docker-compose
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip  
pip install -r requirements.txt
```

### 2. Configurar permissoes do Docker
```sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R
```

### 3. Configurar o banco de dados
```sh
make create_mongodb
```
ou
```sh
docker run -d -p 27017:27017 --name mongo-alfa3bd-debug mongo:latest
```

## Rodar o Projeto
### 1. Rodar o Banco de dados
Somente da primeira vez é necessário configurar o banco. 
Das próximas vezes pode-se inicializá-lo com:
```sh
make start_mongodb
```
ou
```sh
docker start alfa3bd-mongo
```

### 3. Rodar o Servidor django
```sh
python manage.py runserver
```
ou clicar em "Run and Debug(Ctrl+Shift+D)" no vscode.

### 4. Acessar a API
Rota: localhost:8000

Para consumir a api utilize a aplicação do frontend (alfabd3_frontend)

# Referencias do projeto backend
- https://www.django-rest-framework.org
- https://www.mongodb.com/compatibility/mongodb-and-django
- https://sourcery.blog/how-to-build-api-with-django-rest-framework-and-mongodb/
- https://www.howtogeek.com/devops/how-to-run-mongodb-in-a-docker-container/
- https://docs.docker.com/engine/install/linux-postinstall/
- https://dev.to/thepylot/add-mongodb-and-postgresql-in-django-using-docker-55j6