#!/bin/bash
read -s -p "Password: " password
echo $password > /tmp/sudo.password
echo $password
