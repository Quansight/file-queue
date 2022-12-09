FROM python:3.10

COPY ./ /opt/file-queue/

RUN pip install /opt/file-queue/

CMD ["file-queue-worker"]
