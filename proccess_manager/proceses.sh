#!/bin/bash
procese=`ps -e | tr -s " " | cut -f2,5 -d" " | tr " " ":" | tail -n +2`
IFS=" "
for p in $procese
do
    echo $p
done

