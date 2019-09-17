import serial
import time
import numpy as np

class Prologix(object):

    def __init__(self, port, baud=9600, timeout=3):
        self.inst = serial.Serial(port, baudrate=baud, timeout=timeout)
        if self.inst.in_waiting:
            _junk = self.inst.read(self.inst.in_waiting)
        self.inst.write('++mode 1\r'.encode('utf-8'))
        self.inst.flush()
        self.inst.write('++auto 0\r'.encode('utf-8'))
        self.inst.flush()

    def open_instrument(self, gpib_address):
        return Instrument(gpib_address, self.inst)

class Instrument(object):

    def __init__(self, gpib, serial_object):
        self.inst = serial_object
        self.gpib = gpib

    def set_address(self):
        self.inst.write('++addr {}\r'.format(self.gpib).encode('utf-8'))
        self.inst.flush()


    def write(self, asciiMessage):
        self.set_address()
        asciiMessage += '\r'
        message = asciiMessage.encode('utf-8')
        self.inst.write(message)
        self.inst.flush()

    def read(self):
        self.set_address()
        response = bytes()
        self.inst.write('++read\r'.encode('utf-8'))
        self.inst.flush()
        time.sleep(.1)
        while self.inst.in_waiting:
            response += self.inst.read(self.inst.in_waiting)
            time.sleep(.1)
        return response

    def query(self, asciiMessage):
        self.write(asciiMessage)
        time.sleep(.1)
        response = self.read()
        return response

    def query_ascii_values(self, asciiMessage):
        response = self.query(asciiMessage)
        response_list = response.decode('ascii').split(',')
        return np.array([float(response_list[i]) for i in range(len(response_list))])


