#!/bin/bash
# chattr +a /www/storage/logs
# chattr +a /www/storage/framework/sessions




echo $FLAG > /flag
python3 /app/app.py
