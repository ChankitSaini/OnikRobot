FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get upgrade -y  && \
    apt-get install --no-install-recommends -y nodejs \
    npm && rm -rf /var/lib/apt/lists/*
RUN apt-get install --no-install-recommends npm -y
RUN apt-get install --no-install-recommends git curl python3-pip ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install --no-install-recommends -y nodejs
RUN npm install -g npm@7.22.0
RUN npm i -g npm

COPY . /py
WORKDIR /py

RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD python3 -m onik
