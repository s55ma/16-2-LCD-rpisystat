#!/bin/bash

#Network speed data calculations
    R1=$(cat /sys/class/net/eth0/statistics/rx_bytes)
    sleep 1
    R2=$(cat /sys/class/net/eth0/statistics/rx_bytes)
    RBPS=$(expr $R2 - $R1)
    RKBPS=$(expr $RBPS / 1024)

    network_in=$RKBPS

    printf "$network_in\n"


