FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip install -r requierements.txt

WORKDIR /random

COPY . .

RUN pytest

CMD ["python3", "main.py"]

