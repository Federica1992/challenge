#!/usr/bin/bash

(crontab -l || true; echo "00 23 * * 7 rsync -a -rsh=ssh /home/user user@192.168.1.100:/home/backup") | crontab -
