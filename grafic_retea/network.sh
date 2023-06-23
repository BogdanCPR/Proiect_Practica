#!/bin/bash
ifstat -S -T 1 1 | tail -1 | awk '{print $1/1000 "\t" $2/1000}'


