#!/bin/bash
# Eliminamos ficheiros .pcap de más de 3 días
find /var/log/tshark/ -name "*.pcap" -type f -mtime +3 -exec rm -f {} \;
# Añadimos permisos 755 a todos los ficheros
chmod 755 /var/log/tshark/*
