FROM python:3.11-bullseye

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y supervisor && \
    pip install -r requirements.txt

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8501
EXPOSE 10000

CMD ["/usr/bin/supervisord"]
