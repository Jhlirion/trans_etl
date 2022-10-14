FROM python:3.10

ENV PYTHONNUNBUFFERED 1
RUN pip install --upgrade pip

COPY ./requirements.txt . 
RUN pip install -r requirements.txt

COPY ./ETL .
RUN /ETL/main.py