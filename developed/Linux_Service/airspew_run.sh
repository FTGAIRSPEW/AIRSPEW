#!/bin/sh 
# Execute and log the output of the script
sudo /etc/init.d/airspew.sh 2>&1 | tee /home/debian/airspew.log
