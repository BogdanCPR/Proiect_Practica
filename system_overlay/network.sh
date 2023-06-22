#!/bin/bash
echo "Network:"
echo "KB/s Download	 KB/s Upload"
ifstat -S 1 1 | tail -1
