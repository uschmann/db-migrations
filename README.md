# build container

```bash
docker build . -t db-migrations
```

# configure .env
```bash
cp .env.example .env
```

# Run migratione
```bash
docker run --user $(id -u):$(id -g) --add-host=host.docker.internal:host-gateway --env-file ./.env -v ./sql:/app/sql db-migrations python app.py migrate
```

# Run container and mount app for development
```bash
docker run -it --user $(id -u):$(id -g) --add-host=host.docker.internal:host-gateway -v .:/app --env-file ./.env db-migrations bash
```

# Rollback migrations
```bash
cp .env.example .env
docker run -it --add-host=host.docker.internal:host-gateway --env-file ./.env db-migrations python migrate.py --rollback
```

# Run sql plus in container
```bash
docker run -it --add-host=host.docker.internal:host-gateway db-migrations sqlplus auschmann/secret@host.docker.internal:1522/FREE
```