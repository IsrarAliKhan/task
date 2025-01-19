FROM python:3.7-slim

WORKDIR /app

ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app/

RUN python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
