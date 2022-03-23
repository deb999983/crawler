FROM python:3.9.7-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache --virtual .build-deps gcc musl-dev mariadb-connector-c-dev \
    && pip install --upgrade pip \
    && pip install mysqlclient \
    && apk del .build-deps \
    && apk add --no-cache -q git ffmpeg mariadb-connector-c

## Install dependencies.
RUN pip install --upgrade pip && \
    pip install urllib3 requests pytz \
    Django==3.2.* djangorestframework \
    drf-spectacular \
    gunicorn


ARG INSTALL_DIR=/src
ENV PYTHONPATH=$INSTALL_DIR
ENV INSTALL_DIR=$INSTALL_DIR

WORKDIR $INSTALL_DIR

COPY requirements.txt .


### Install dependencies
RUN pip install -r requirements.txt

### Pull code
COPY . .

## Port expose
EXPOSE 8000

## Run entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
