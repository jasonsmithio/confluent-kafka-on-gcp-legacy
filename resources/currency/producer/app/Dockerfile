FROM python:3.7-slim

ADD . .

RUN apt-get update && \
    pip install -r requirements.txt

ENTRYPOINT ["python", "-u", "/producer.py"]