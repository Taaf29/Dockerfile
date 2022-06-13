FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3

RUN apt-get install python3-pip 

RUN pip install -r requierements.txt

WORKDIR /random

COPY . .

RUN pytest

CMD [ "python3","main.py" ]

