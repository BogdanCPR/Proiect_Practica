#!/bin/bash
echo "Specificatii sistem:"
modelProcesor=`lscpu | grep "Model name" | sed s/"Model name: "//`
modelProcesor="Model CPU: $modelProcesor"

memorieRAM=`free -h | tr -s " " | cut -f2 -d" " | tail -2 | head -1`
memorieRAM="Memorie RAM: $memorieRAM"

disk=`df -h | grep sda3 | tr -s " " | cut -f2 -d" "`
disk="Stocare: $disk"

SO=`lsb_release -a | grep Description | tr -s " \t" | sed "s/Description:\t//"`
SO="Versiune SO: $SO"
user=`whoami`

echo $modelProcesor
echo $memorieRAM
echo $disk
echo $SO
echo "Utilizator activ: $user"
