# 🐘 Running PostgreSQL with Docker

## Starting a PostgreSQL Container

Run this command to start PostgreSQL locally in a Docker container:

```bash
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecret -p 5432:5432 -d postgres
````

* `--name my-postgres`: names the container
* `-e POSTGRES_PASSWORD=mysecret`: sets the default password
* `-p 5432:5432`: maps container port to host port
* `-d`: runs container in detached mode

## Persist Data with Volumes (Optional)

```bash
docker volume create pgdata

docker run --name my-postgres \
  -e POSTGRES_PASSWORD=mysecret \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 -d postgres
```

This stores your database files persistently outside the container.

## Connect to PostgreSQL

* Use clients like `psql`, pgAdmin, or DBeaver
* Connection details:

  * Host: `localhost`
  * Port: `5432`
  * User: `postgres`
  * Password: `mysecret`

