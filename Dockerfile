FROM python:3.9.18-slim

COPY start.sh /scripts/start.sh
COPY app/ /app/
WORKDIR /app
ENTRYPOINT ["/scripts/start.sh"]
