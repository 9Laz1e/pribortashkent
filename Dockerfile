FROM python:3.10.5 

WORKDIR /var/www/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /var/www/app

RUN pip install -r requirements.txt

COPY . /var/www/app