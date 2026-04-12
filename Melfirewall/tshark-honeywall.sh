#!/bin/bash
# Creamos el directorio en el que guardaremos las capturas
sudo mkdir -p /var/log/tshark
sudo chmod 755 /var/log/tshark
# Capturamos en la interfaz externa con un límite de 
# 24 ficheiros rotados cada 1 hora 
sudo tshark -i enp0s3 -w /var/log/tshark/enp0s3-$(date +%Y-%m-%d_%H.%M).pcap -b duration:3600 -b files:24 &
# Capturamos en la interfaz interna con un límite de 
# 24 ficheiros rotados cada 1 hora 
sudo tshark -i enp0s8 -w /var/log/tshark/enp0s8-$(date +%Y-%m-%d_%H.%M).pcap -b duration:3600 -b files:24 &
# Esperar para que los procesos en background sigan vivos
wait
