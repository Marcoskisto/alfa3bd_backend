# **Projeto ALFA3-BD**


## Rodar o projeto em producao
### 1. Configurar Docker
```sh
sudo apt install docker docker-compose
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R
```
### 2. Rodar os containers
```sh
sudo docker-compose up
```

## Rodar o projeto em Desenvolvimento
### Backend
1. Rodar o Banco de dados mongo - [Readme.md do alfa3bd_backend](./alfa3bd_backend/Readme.md)
2. Rodar o backend em django - [Readme.md do alfa3bd_backend](./alfa3bd_backend/Readme.md)
### Frontend
Rodar o frontend - [Readme.md do alfa3bd_backend](./alfa3bd_frontend/README.md)