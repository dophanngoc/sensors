#!/usr/bin/env python3

import serial
import logging
import datetime
import numpy as np

from utils import log

LOGGER = log.logging_define()

serialTTY = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = None
)
class DataFrame:
    def __init__(self):
        pass
    @staticmethod
    def get_data():
        raw_data = serialTTY.read().hex()
        return raw_data
    @staticmethod
    def check_header():
        while True:
            get_val1 = DataFrame.get_data()
            get_val2 = DataFrame.get_data()
            if(get_val1 == '53' and get_val2 == '59'):
                return True
            else:
                continue 
    @staticmethod         
    def is_tailer():
        tail_sign_count = 0
        while True:
            val_next = DataFrame.get_data()
            if(val_next == '43'):
                return val_next, tail_sign_count, True
            if(val_next == '54'):
                tail_sign_count += 1
                continue
            return val_next, tail_sign_count, False
    @staticmethod
    def data_store():
        frame_new = []
        if(DataFrame.check_header):
            while True:
                get_next = DataFrame.get_data() 
                frame_new.append(get_next)
                if(get_next == '54'):
                     to_add_data, sign_count, tail_ok = DataFrame.is_tailer() 
                     for i in range(sign_count):
                         frame_new.append('54')
                     if(tail_ok):
                         frame_new.append('43')
                         break
                     frame_new.append(to_add_data)
            if(frame_new[3] == '01'):
                 LOGGER.info(frame_new) 

def main():
    data_frame = DataFrame()
    while True:
        data_hex = data_frame.data_store()

if __name__ == '__main__':
    main()


