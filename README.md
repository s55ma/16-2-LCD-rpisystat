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
6. chmod +x *.sh *.py
7. Run rpisystat.py
8. Detailed instructions: https://s55ma.radioamater.si/2015/11/16/raspberrypi-2-16x2-lcd-with-system-stats-script

Video: https://www.youtube.com/watch?v=5YkLTBd5-bw

![alt tag](https://raw.githubusercontent.com/s55ma/16-2-LCD-rpisystat/master/img/16x2_lcd_display_rpi2.jpg)
