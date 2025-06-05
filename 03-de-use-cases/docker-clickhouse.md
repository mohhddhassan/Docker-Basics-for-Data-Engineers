````markdown
# ⚡ Running ClickHouse with Docker

## Start ClickHouse Container

Use this command to run ClickHouse quickly:

```bash
docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 yandex/clickhouse-server
````

* `-d`: runs container in detached mode
* Ports:

  * `8123` for HTTP interface
  * `9000` for native client protocol

## Verify the Container is Running

```bash
docker logs clickhouse-server
```

Look for messages indicating the server started successfully.

## Querying ClickHouse

* Use the official [clickhouse-client](https://clickhouse.com/docs/en/interfaces/cli/)
* Or tools like [Tabix](https://tabix.io/) for web UI


