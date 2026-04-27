#!/bin/bash
rsync --inplace -arz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 22" root@172.16.0.101:/var/log/mailoney /var/log/hp2/mailoney
rsync --inplace -arz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 22" root@172.16.0.101:/var/log/miniprint /var/log/hp2/miniprint
rsync --inplace -arz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 22" root@172.16.0.101:/var/log/adbhoney /var/log/hp2/adbhoney
chmod -R 755 /var/log/hp2
