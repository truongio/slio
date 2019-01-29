FROM python:3.7-alpine3.8

ENV FLASK_APP=sl_time

ADD requirements.txt /requrements.txt

RUN pip install -U pip
RUN pip install -r requrements.txt

ADD sl_time.py /sl_time.py
ADD config.yaml /config.yaml

# Note PORT is set by heroku
CMD flask run --host 0.0.0.0 -p ${PORT}