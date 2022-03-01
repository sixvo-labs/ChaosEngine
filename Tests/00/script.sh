#!/usr/bin/bash

while true
do
    curl 127.0.0.1:80/snapshot
    curl 127.0.0.1:80/snapshot >> ./log.txt
    echo "\n" >> ./log.txt
    sleep 0.5
done
