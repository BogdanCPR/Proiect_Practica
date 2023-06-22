#!/bin/bash
echo "Network:"
echo "KB/s in	   KB/s out"
ifstat -S 1 1 | tail -1 


