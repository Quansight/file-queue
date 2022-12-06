FROM python:3.10

COPY . /opt/

ENV PYTHONPATH=$PYTHONPATH:/opt/

RUN pip install dask distributed
