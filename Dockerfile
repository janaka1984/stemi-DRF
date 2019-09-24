FROM python:37

MAINTAINER Janaka Weerarathna

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r stemirestapi/requirments.txt

EXPOSE 80

CMD ["python","app.py"]