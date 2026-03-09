# Portable Data Stack with SQLMesh

This application is a containerized Analytics suite for an imaginary company selling postcards. The company sells both directly but also through resellers in the majority of European countries.

## Stack

- Docker (docker compose)
- DuckDB
- SQLMesh using dbt adapter
- Superset

## Interested in the data model?

Generation of example data and the underlying dbt-core model is available in the [postcard-company-datamart](https://github.com/cnstlungu/postcard-company-datamart) project.

![Data Model](resources/data_model.png "Data Model")


## For other stacks, check the below:
- [portable-data-stack-dagster](https://github.com/cnstlungu/portable-data-stack-dagster)
- [portable-data-stack-airflow](https://github.com/cnstlungu/portable-data-stack-airflow)
- [portable-data-stack-mage](https://github.com/cnstlungu/portable-data-stack-mage)
- [portable-data-stack-bruin](https://github.com/cnstlungu/portable-data-stack-bruin)

### System requirements
* [Docker](https://docs.docker.com/engine/install/)

## Setup

1. Rename `.env.example` file to `.env` and set your desired Superset password. Remember to never commit files containing passwords or any other sensitive information.

2. Rename `shared/db/datamart.duckdb.example` to `shared/db/datamart.duckdb` or init an empty database file there with that name.

3. With **Docker engine** installed, change directory to the root folder of the project (also the one that contains docker-compose.yml) and run

    `docker compose up --build`

4. Once the Docker suite has finished starting, you will see the output of the SQLMesh plan & apply commands, which run the dbt core models against DuckDB.

![SQLMesh plan & apply](resources/sqlmesh_plan_apply.png "SQLMesh plan & apply")

5. To explore the data and build dashboards you can open the [Superset interface](http://localhost:8088)


### Demo Credentials

Demo credentials are set in the .env file mentioned above.

### Ports exposed locally
* SQLMesh: 8000
* Superset: 8088

Generated parquet files are saved in the **shared/parquet** folder.

The data is fictional and automatically generated. Any similarities with existing persons, entities, products or businesses are purely coincidental.

### General flow

1. Test data is generated as parquet files using Python (generator)
2. Data is imported from parquet files to the staging area in the Data Warehouse (DuckDB)
3. The data is modelled, building fact and dimension tables, loading the Data Warehouse using SQLMesh (with the dbt adapter for model compatibility)
4. Analyze and visually explore the data using Superset or directly querying the datamart via the SQL IDE provided by SQLMesh

For Superset, the default credentials are set in the .env file: user = admin, password = admin


## Overview of architecture

The Docker process will begin building the application suite. The suite is made up of the following components, each within its own Docker container:
* **generator**: a collection of Python scripts that generate and export the example data, using the [postcard-company-datamart](https://github.com/cnstlungu/postcard-company-datamart) project
* **sqlmesh-dbt**: the data model, sourced from the [postcard-company-datamart](https://github.com/cnstlungu/postcard-company-datamart) project
* **superset**: the web-based Business Intelligence application used to explore the data; exposed on port 8088.


After the models have been applied you can either analyze the data using the querying and visualization tools provided by Superset (available locally on port 8088), or query the Data Warehouse (available as a DuckDB database).

![Apache Superset](resources/superset.png "Superset")
