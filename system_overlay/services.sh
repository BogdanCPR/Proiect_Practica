#!/bin/bash
nrlinii=`systemctl list-units --type=service --state=running | wc -l`
systemctl list-units --type=service --state=running | head -n $(($nrlinii - 5))
