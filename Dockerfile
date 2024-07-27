FROM python:3.10

#install sqlplus
RUN apt update && apt install libaio1

RUN wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-basic-linux.x64-21.4.0.0.0dbru.zip &&\
    wget https://download.oracle.com/otn_software/linux/instantclient/214000/instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip  &&\
    mkdir -p /opt/oracle &&\
    unzip -d /opt/oracle instantclient-basic-linux.x64-21.4.0.0.0dbru.zip &&\
    unzip -d /opt/oracle instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip &&\
    rm instantclient-basic-linux.x64-21.4.0.0.0dbru.zip &&\
    rm instantclient-sqlplus-linux.x64-21.4.0.0.0dbru.zip

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_4
ENV PATH=$LD_LIBRARY_PATH:$PATH

RUN mkdir /app
COPY ./requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "migrate.py", "--help"]