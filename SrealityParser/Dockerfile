FROM python:bullseye

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install sqlalchemy==1.4.44
RUN pip install psycopg2==2.9.5
RUN pip install scrapy==2.7.0
RUN pip install pandas==1.5.1

COPY . .

CMD ["python", "main.py"]