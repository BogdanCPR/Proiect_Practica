#!/bin/bash
PID=`ps -eo pid,%cpu --sort=-%cpu | head -n 2 | tail -n 1 | awk '{print $1}'`

echo $PID
PROCESS=`ps -e | egrep $PID | tr -s " " | cut -f5 -d" "`
echo $PROCESS
