FROM python:3.6

WORKDIR /app

COPY ./requirement.txt /app/

COPY ./src /app

RUN apt-get update && apt-get install -y python3-tk graphviz

RUN pip install -r requirement.txt

ENTRYPOINT ["/usr/local/bin/python3.6"]

CMD ["main.py"]
