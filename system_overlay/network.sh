#!/bin/bash
echo "Network:"
echo "MB/s Download	 MB/s Upload"
ifstat -S -T 1 1 | tail -1 | awk '{print $1/1000 "         " $2/1000}'



