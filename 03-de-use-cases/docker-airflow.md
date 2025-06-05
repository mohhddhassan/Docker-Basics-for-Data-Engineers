````markdown
# 🔄 Running Apache Airflow with Docker

## Quick Start Using Official Docker Compose

Airflow official repo provides a docker-compose setup:

```bash
git clone https://github.com/apache/airflow.git
cd airflow
cp .env.example .env
docker compose up airflow-init
docker compose up
````

* This sets up Airflow with all dependencies in containers
* Runs scheduler, webserver, and database

## Access Airflow Web UI

* Open browser: [http://localhost:8080](http://localhost:8080)
* Default credentials:

  * Username: `admin`
  * Password: `admin`

## Notes

* First startup may take some time as images download
* You can customize DAGs by mounting volumes or modifying configs
* Docker Compose must be installed on your system

