FROM python:3.11.0


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /payments
ADD . /payments
COPY templates /payments/templates/

RUN pip install -r requirements.txt