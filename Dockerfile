FROM ubuntu:16.04
RUN apt update && apt-get install -y software-properties-common redis-server curl
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt update && apt install -y python3.6
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
COPY . /opt
RUN pip install -r /opt/requirements.txt
ENV REDIS_URL=redis://localhost
