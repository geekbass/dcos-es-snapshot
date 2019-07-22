FROM python:latest
RUN pip install elasticsearch
COPY elastic-s3-snapshot.py
CMD python elastic-s3-snapshot.py