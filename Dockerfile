FROM python:3.8-alpine
RUN mkdir /src
WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY /src /src
CMD ["python3", "main.py"]

