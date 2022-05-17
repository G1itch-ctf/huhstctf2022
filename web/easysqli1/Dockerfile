From ubuntu20.04_mysql8:mysql8



RUN apt-get update -y

RUN apt install nodejs npm -y && \
    npm install -g pm2 && \
    mkdir /var/app/


ADD ./html /var/app/
RUN usermod -d /var/lib/mysql/ mysql

COPY flag.txt /root/flag.txt
COPY start.sh /root/start.sh
RUN chmod +x /root/start.sh
ENTRYPOINT cd /root; ./start.sh
EXPOSE 3000
