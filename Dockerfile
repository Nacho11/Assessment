FROM python:3.6.3

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

ADD finalized_model.sav /app

ADD api.py /app

RUN pip3 install -r requirements.txt

CMD  ["python", "./api.py"]
