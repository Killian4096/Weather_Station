#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, pty, serial

master, slave = pty.openpty()
s_name = os.ttyname(slave)

ser = serial.Serial(s_name)

print(s_name)

# To Write to the device
while(1):
    a = os.read(master,1000)
    print(a)

