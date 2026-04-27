#!/bin/bash
rsync --inplace -arz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 22" root@172.16.0.100:/var/log/wordpress /var/log/hp1/wordpress
rsync --inplace -arz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 22" root@172.16.0.100:/var/log/cowrie /var/log/hp1/cowrie
chmod -R 755 /var/log/hp1
