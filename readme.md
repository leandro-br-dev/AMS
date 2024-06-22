# Crie uma rede Docker para facilitar a comunicação entre contêineres
docker network create agent_network

# Inicie um contêiner PostgreSQL
docker run --name postgres -e POSTGRES_USER=xxx -e POSTGRES_PASSWORD=xxx -e POSTGRES_DB=xxx -p 5432:5432 --network=agent_network -d postgres

# Inicialize as migrações
flask db init

# Crie uma migração inicial
flask db migrate -m "Initial migration"

# Aplique a migração
flask db upgrade

