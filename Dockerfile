FROM python:3.13-slim-bookworm

RUN groupadd -g 1000 django && \
    useradd -u 1000 -g django -m django

WORKDIR /home/django

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY --chown=django:django . .

RUN chmod +x /home/django/docker-entrypoint.sh && \
    mkdir -p /home/django/media /home/django/staticfiles && \
    chown -R django:django /home/django/media /home/django/staticfiles

ENTRYPOINT ["/home/django/docker-entrypoint.sh"]

CMD ["gunicorn"]

EXPOSE 8000

USER django

VOLUME /home/django/media /home/django/staticfiles
