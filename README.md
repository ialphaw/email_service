# Email Service

This is an Email Service app written with FastAPI

# What was the problem

When you want to send your emails, There might have been a fluctuation in the mail server you are using, so there is always better to use more than one mail service. This app will use [Sendgrid](https://sendgrid.com/) as its primary mail server if it fails, [Mailgun](https://www.mailgun.com/) will be replaced. 

## Installation

Use the package manager [Poetry](https://python-poetry.org/) to run Email Service. Just run the below command to install all the dependencies.

```bash
poetry install
```

## Usage

First, you should generate a .env file based on .env.sample you can find in the app.

next, [Celery](https://docs.celeryq.dev/) is needed for this app. Just run the below command.

```bash
celery -A core.celery worker -E -l info --logfile=celery.log -B --detach
```

This app use [Uvicorn](https://www.uvicorn.org/) for its ASGI server. you can start the app with the below command.

```bash
uvicorn main:app --reload
```

Or instead of above steps, just run below command:

```bash
docker-compose up -d --build
```
