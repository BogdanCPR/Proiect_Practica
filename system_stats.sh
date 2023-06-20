#!/bin/bash
clear
while true
do
	
    cpu=`top -bn1 -w 512 | grep "Cpu(s)" | awk '{print $2+$4+$6}'`
    mem=`free -ht -t | grep "Total" | awk '{print $3/$2 * 100.0}'`
    disk=`df -hP | egrep -w "/" | egrep -wo "[0-9]*%" | tr -d "%"`
    clear
    printf "CPU Usage:\t%.1f%%      \nMemory Usage:\t%.1f%%   \nDisk Usage:\t%d%%   " $cpu $mem $disk
    sleep 0.5
    #printf "\033[F\033[F"
done
