#!/usr/bin/env python3
"""
    File:   simulate_mw_ppg_signal.py
    Author: Vlad Baciu
    Started: 03.10.2022
    Edited: 03.10.2022
"""

from time import sleep
import serial


# COM1 should be a virtual port paired with COM2
ser = serial.Serial("COM1", 9600)

ser.set_buffer_size(rx_size = 128000, tx_size = 128000)
# Read line
while True:

    with open('test.txt', 'r') as f:
        for line in iter(f.readline, ''):
            ser.write(line.replace("\n", ",").encode() + line.replace(" ", ",").encode())
            #print(line.replace("\n", ",").encode() + line.replace(" ", ",").encode())
            sleep(0.008)

