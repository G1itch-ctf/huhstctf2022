FROM ubuntu:18.04

COPY ./files/sources.list /etc/apt/sources.list
RUN \
        apt-get update && \
        apt-get install -y vim && \
	apt-get install -y curl && \
        apt-get install -y wget && \
        apt install -y python3 && \
	apt-get install -y python3-pip && \
        pip3 install flask

RUN mkdir /app


COPY ./source /app

COPY ./files/start.sh  /root/

RUN \
        chmod 755 /root/start.sh && \
        chmod +x /root/start.sh

CMD ["bash","/root/start.sh"]
