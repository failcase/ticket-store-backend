FROM python:3.13-slim-bookworm

RUN useradd --create-home django

WORKDIR /home/django

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY --chown=django:django . .

RUN chmod +x /home/django/docker-entrypoint.sh

ENTRYPOINT ["/home/django/docker-entrypoint.sh"]

CMD ["gunicorn"]

EXPOSE 8000

USER django
