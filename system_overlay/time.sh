#!/bin/bash


lastlog=`last | head -n 1 | tr -s " " | cut -f5,6,7 -d" "`
echo "Last login: $lastlog"


lastlog_ts=$(date -d "$lastlog" +%s)
now=$(date +%s)
seconds=$((now - lastlog_ts))

days=$((seconds / 86400))
seconds=$((seconds % 86400))
hours=$((seconds / 3600))
seconds=$((seconds % 3600))
minutes=$((seconds / 60))
seconds=$((seconds % 60))

printf "Time since last login: %d days, %02d:%02d:%02d\n" $days $hours $minutes $seconds
