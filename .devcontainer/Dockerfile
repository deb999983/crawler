FROM python:3.9.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create user
ARG USERNAME=crawler_user
ARG USER_UID=501
ARG USER_GID=20

# Create the user
RUN useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

### Install base dependencies
RUN \
 apt update && \
 apt install netcat lsof libpq-dev python3-dev gcc -y

USER crawler_user

### Setup work dir
WORKDIR /workspaces/crawler
ENV PYTHONPATH=/workspaces/crawler

### Install all dependencies
COPY worker/requirements.txt worker/requirements.txt
COPY web_server/requirements.txt web_server/requirements.txt

RUN \    
    pip3 install -r web_server/requirements.txt && \
    pip3 install -r worker/requirements.txt

### Pull code
COPY . .

## Port expose
EXPOSE 8000
