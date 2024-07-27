# build container

```bash
docker build . -t db-migrations
```

# configure .env
```bash
cp .env.example .env
```

# Run migrations
```bash
docker run -it --add-host=host.docker.internal:host-gateway --env-file ./.env db-migrations python migrate.py
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