#!/bin/bash
# chattr +a /www/storage/logs
# chattr +a /www/storage/framework/sessions




#echo $FLAG > /flag
sed -i s/flagtest/$FLAG/g /var/www/html/assets/main/index.bc778.js
/etc/init.d/apache2 restart
tail -f /var/log/apache2/access.log
