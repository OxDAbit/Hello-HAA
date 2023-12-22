"""
-------------------------------------------------------------------------------
Name:     detect_usb.py
Purpose:  Detección de dispositivos USB conectados
Version:  v0.0.1
Author:   David Alvarez Medina
Created:  22/12/2023
-------------------------------------------------------------------------------
"""
import glob
print(glob.glob('/dev/tty.*'))
