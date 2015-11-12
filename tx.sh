#Network speed data calculations
    T1=$(cat /sys/class/net/eth0/statistics/tx_bytes)
    sleep 1
    T2=$(cat /sys/class/net/eth0/statistics/tx_bytes)
    TBPS=$(expr $T2 - $T1)
    TKBPS=$(expr $TBPS / 1024)

network_out=$TKBPS

    printf "$network_out\n"

