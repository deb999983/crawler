FROM python:3.9.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

## Install dependencies.
RUN \
 apt update && \
 apt install netcat lsof libpq-dev python3-dev gcc -y && \
 pip install -r requirements.txt

ARG INSTALL_DIR=/workspaces/worker
ENV INSTALL_DIR=$INSTALL_DIR

ENV PYTHONPATH=$INSTALL_DIR/src
WORKDIR $INSTALL_DIR

### Pull code
COPY . .

## Run entrypoint.sh
ENTRYPOINT ["scripts/entrypoint.sh"]
