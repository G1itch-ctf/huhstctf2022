FROM ubuntu:18.04

COPY ./files/sources.list /etc/apt/sources.list
RUN \
        apt-get update && \
        apt-get install -y apache2


RUN rm -rf /var/www/html/*
COPY ./source /var/www/html/

COPY ./files/start.sh  /root/

RUN \
        chmod 755 /root/start.sh && \
        chmod +x /root/start.sh

CMD ["bash","/root/start.sh"]
