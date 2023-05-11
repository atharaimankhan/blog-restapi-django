FROM python:3.11.0
ENV PYTHONUNBUFFERED 1
WORKDIR /blog-api
COPY requirements.txt /blog-api/requirements.txt
RUN pip install -r requirements.txt
COPY . /blog-api