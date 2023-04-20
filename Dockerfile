
FROM python:3.9.16-slim-buster
RUN mkdir /app && chmod 777 /app
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg megatools
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD gunicorn app:app & bash startup.sh
