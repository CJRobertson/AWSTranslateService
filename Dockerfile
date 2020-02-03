FROM python:3.7.6-alpine

RUN adduser -D translate

WORKDIR /home/translate

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY  config.py boot.sh ./
RUN chmod a+x boot.sh

RUN chown -R translate:translate ./
USER translate

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
