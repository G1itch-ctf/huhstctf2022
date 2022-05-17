#!/bin/bash
# chattr +a /www/storage/logs
# chattr +a /www/storage/framework/sessions




echo $FLAG > /root/flag


/etc/init.d/apache2 restart
service mysql start
java -jar /Springboot-1.0-SNAPSHOT.jar
rm -rf /root/start.sh
