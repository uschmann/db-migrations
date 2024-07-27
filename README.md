# build container

```bash
docker build . -t db-migrations
```

# Run container
```bash
docker run -it --add-host=host.docker.internal:host-gateway pythontest sqlplus auschmann/secret@host.docker.internal:1522/FREE
```