# Task API

## Prerequisites

- Python >= 3.7 [⤴](https://www.python.org/downloads/release/python-370/)
- Pipenv [⤴](https://pipenv.pypa.io/en/latest/installation.html)
- Taskfile [⤴](https://taskfile.dev/installation/)
- Create `.env` from `.env.sample`

## Local Setup

- Execute the following command to install the dependencies

    ```shell
    task setup
    ```

- Execute the following command to run the migrations

    ```shell
    task migrate
    ```

- Execute the following command to create a super user

    ```shell
    task user
    ```

- Execute the following command to run the application

    ```shell
    task run
    ```

## Docker Setup

- Execute the following command to run the container

    ```shell
    docker-compose up -d
    ```

- Execute the following command to stop the container

    ```shell
    docker-compose down
    ```

## Swagger Endpoint

```shell
 http://<host>:<port>/api/schema/swagger-ui/
 ```

## Project Structure

```shell
./
├── apps/
│   ├── common/
│   │   └── permissions.py
│   ├── labels/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── tasks/
│       ├── migrations/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── core/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env.sample
├── Dockerfile
├── Pipfile
├── README.md
├── Taskfile.yml
├── docker-compose.yml
├── manage.py
└── requirements.txt
```
