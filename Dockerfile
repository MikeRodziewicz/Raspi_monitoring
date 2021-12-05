FROM python:3.8-alpine
ENV GPIOZERO_PIN_FACTORY=native
RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY /src .
CMD ["python3", "main.py"]

