FROM python:3.10-alpine

LABEL MAINTAINER="Gabriel Saudade gabrielfsaudade@ua.pt"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY app/* /app/

COPY ./secret /tmp/

RUN pip install gunicorn

# Creats a user with access only to /var/www
RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD ["python3", "-m", "app"]
