FROM python:3.9-slim-bullseye as base

RUN apt-get update && apt-get install -y cron

# Añade el archivo crontab al directorio crontab del sistema
# COPY crontab /etc/cron.d/simple-cron
#
# # Da permisos al archivo crontab
# RUN chmod 0644 /etc/cron.d/simple-cron
#
# # Aplica el archivo crontab
# RUN crontab /etc/cron.d/simple-cron

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create app directory
WORKDIR /src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

# ---- Copy Files/Build ----
FROM base

WORKDIR /src

COPY . /src

RUN chmod -R 777 /src
