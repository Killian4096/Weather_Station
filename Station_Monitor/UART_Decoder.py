#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import zmq


import sys
import zmq
import numpy as np

import math

NO_SIGNAL = 0
SIGNAL = 1
STOP_BIT = 2

BIT_COUNT = 8
STOP_BITS = 20

SAMP_FREQ = 2.048 * 10.0**6
DECIM = 64.0
BAUD = 9600.0

PORT = 3000

SAMP_PERIOD = DECIM/(SAMP_FREQ)
BAUD_PERIOD = 1.0/BAUD

class UART_Processor:
    def __init__(self):
        self.bit_stream = np.array([1])
        self.current_num = 0
        self.STATE = NO_SIGNAL
        self.current_bits = 0
        self.current_time = 0.0
        self.data_stream = np.array([])
        self.stop_bits = 0
    
    def stream(self, array):
        self.bit_stream = np.append(self.bit_stream, array)
    
    def process_signal(self):
        while not(len(self.bit_stream) == 0):
            bit = self.bit_stream[0]
            self.bit_stream = self.bit_stream[1:]
            if self.STATE == NO_SIGNAL and not(bit):
                self.STATE = SIGNAL
                self.current_time = 0.0
            elif self.STATE == SIGNAL:
                self.current_time += SAMP_PERIOD
                if(self.current_time>=BAUD_PERIOD):
                    self.current_time -= BAUD_PERIOD
                    if bit:
                        self.current_num = (1<<(BIT_COUNT-1)) | (self.current_num >> 1)
                    else:
                        self.current_num = (self.current_num >> 1)
                    self.current_bits+=1
                    if(self.current_bits==BIT_COUNT):
                        self.stop_bits = 0
                        self.STATE = STOP_BIT
                        self.data_stream = np.append(self.data_stream, self.current_num)
                        print(self.data_stream)
                        self.current_bits = 0
                        self.current_num = 0
            elif self.STATE == STOP_BIT:
                self.stop_bits += 1
                if self.stop_bits >= STOP_BITS:
                    self.STATE = NO_SIGNAL
        
    def get_next_value():
        number = self.data_stream[0]
        self.data_stream = self.data_stream[1:]
                        

class ZMQ_UART_Connector():
    def __init__(self):

        # Socket to talk to server
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        print ("Collecting updates from weather server...")
        self.socket.connect ("tcp://127.0.0.1:%s" % PORT)

        self.socket.setsockopt_string(zmq.SUBSCRIBE, '')

        self.processor = UART_Processor()
    
    def process_message(self):
        message = self.socket.recv()
        for i in range((int)(len(message)/4)):
            self.processor.stream(np.array(message[i*4]))
        self.processor.process_signal()
    
    def next_value(self):
        if(len(self.processor.data_stream) == 0):
            return None
        number = self.processor.data_stream[0]
        self.processor.data_stream = self.processor.data_stream[1:]
        return number

def main():
    Z = ZMQ_UART_Connector()
    while(True):
        Z.process_message()

#main()