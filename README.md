RaspberryPi 16x2 LCD system information

This Python script will display system parameters to your 16x2 LCD connected to the RaspberryPI.

This script displays:

- Internal IP
- External IP
- CPU temperature
- GPU temperature
- CPU usage
- Memory usage
- Free disk space
- Incoming and outgoing network traffic

How to use:

1. Connect the LCD to RaspberryPi
2. Install all python prerequisites
3. Edit rpisystat.py to match your GPIO pins
4. Edit rpisystat.py to match your network adapter (eth0 or wlan0)
5. Edit rx.sh and tx.sh to match your network adapter (eth0 or wlan0)
6. Run rpisystat.py
