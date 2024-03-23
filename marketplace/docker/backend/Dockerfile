FROM python:3-slim

RUN python3 -m venv /opt/venv/

CMD ["mkdir", "app/web/"]

WORKDIR /app/web/
COPY ./marketplace/backend/ .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/* && \
    python3 -m venv /opt/venv/ && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r /app/web/requirements.txt && \
    chmod +x /app/web/scripts/entrypoint.sh && \
    chmod +x /app/web/scripts/createsuperuser.sh && \
    chmod +x /app/web/scripts/migrations.sh && \
    chmod +x /app/web/scripts/collectstatic.sh && \
    bash /app/web/scripts/migrations.sh && \
    bash /app/web/scripts/collectstatic.sh && \
    bash /app/web/scripts/createsuperuser.sh


CMD ["/app/web/scripts/entrypoint.sh"]