#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 21
lcd_d7        = 22
lcd_backlight = 4
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
							lcd_columns, lcd_rows, lcd_backlight)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

# Internal IP address
cmd1 = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1 | head -n 1"

# External IP address
cmd2 = "wget http://ipinfo.io/ip -qO -"

# Rpi CPU temperature
cmd3 = "cat /sys/class/thermal/thermal_zone0/temp | awk 'NR == 1 { print $1 / 1000}' | cut -c -4"

# Rpi GPU temperature
cmd4 ="/opt/vc/bin/vcgencmd measure_temp | cut -c 6- | cut -c -4"

# CPU usage - print s/4 means divided by four (number of cores)
cmd = "top -bn 1 | awk 'NR>7{s+=$9} END {print s/4}'"

# Memory usage 
cmd6 = "free | awk 'FNR == 3 {print $3/($3+$4)*100}' | cut -c -3"

# Get free disk space
cmd7 = "df -h | awk 'NR==2 { print $3 }'"

# Calculate RX rate
cmd8 ="bash rx.sh"

# Calculate TX rate
cmd9 ="bash tx.sh"

inet = run_cmd(cmd1)
exnet= run_cmd(cmd2)
tempcpu = run_cmd(cmd3)
tempgpu = run_cmd(cmd4)
usagecpu = run_cmd(cmd)
usagemem = run_cmd(cmd6)
freedisk = run_cmd(cmd7)
rx = run_cmd(cmd8)
tx = run_cmd(cmd9)

while 1:
	# Print internal and external IP address
#	lcd.message('%s' % (inet))
#	lcd.message('%s' % (exnet))
#	time.sleep(3.0)
#	lcd.clear()

	# Print Rpi CPU and GPU temperature
#	lcd.message("CPU Temperature: \n"+ str(tempcpu)+ chr(223)+ "C")
#	time.sleep(3.0)
#	lcd.clear()
#	lcd.message("GPU Temperature: \n"+ str(tempgpu)+ chr(223)+ "C")
#	time.sleep(3.0)
#	lcd.clear()

	# Print CPU and Memory Usage
	lcd.message('Cpu %% %s' % (usagecpu))
#	lcd.message('Mem %% %s' % (usagemem))
#	time.sleep(3.0)
#	lcd.clear()

	# Print disk free
 #       lcd.message('Free disk space: \n%s' % (freedisk))
  #      time.sleep(3.0)
   #     lcd.clear()

	# Print network speed
#	lcd.message('Rx KB/s: %s' % (rx))
#	lcd.message('Tx KB/s: %s' % (tx))
#	time.sleep(3.0)
#	lcd.clear()
