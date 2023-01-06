FROM python:latest

WORKDIR /code

COPY . /code/

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry install

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload"]
