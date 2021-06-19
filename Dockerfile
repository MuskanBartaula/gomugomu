FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /vvouch/
COPY requirements.txt /vvouch/
RUN pip install -r requirements.txt
COPY . /vvouch/
