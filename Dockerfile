FROM python:3.5
MAINTAINER Alexander Bykov <alardus@ya.ru>
RUN mkdir -m 777 /code
WORKDIR /code

ADD req.txt /code/
RUN pip install -r req.txt

COPY ./* /code/

CMD ["python", "./client.py"]
