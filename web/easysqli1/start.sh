#!/bin/bash
sleep 1
find /var/lib/mysql -type f -exec touch {} \; && service mysql start

sed -i "s/flagtest/$FLAG/" /var/app/ctf.sql
cat /var/app/ctf.ql
mysqladmin -u root password "tls_tql_111"
mysql -uroot -ptls_tql_111 < /var/app/ctf.sql
rm -f /var/app/ctf.sql

cd /var/app/;pm2 start /var/app/app.js --name my-api

tail -f /etc/passwd
