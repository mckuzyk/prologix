import serial
import time

class prologix(object):

	def __init__(self, gpib, port, baud=9600, timeout=3):
		self.inst = serial.Serial(port, baudrate=baud, timeout=timeout)
		if self.inst.in_waiting:
			_junk = self.inst.read(self.inst.in_waiting)
		self.inst.write('++mode 1\r'.encode('utf-8'))
		self.inst.flush()
		self.inst.write('++auto 0\r'.encode('utf-8'))
		self.inst.flush()
		self.inst.write('++addr {}\r'.format(gpib).encode('utf-8'))


	def write(self, asciiMessage):
		asciiMessage += '\r'
		message = asciiMessage.encode('utf-8')
		self.inst.write(message)
		self.inst.flush()

	def read(self):
		response = bytes()
		self.inst.write('++read\r'.encode('utf-8'))
		self.inst.flush()
		time.sleep(.1)
		while self.inst.in_waiting:
			response += self.inst.read(ser.in_waiting)
			time.sleep(.1)
		return response

	def query(self, asciiMessage):
		self.write(asciiMessage)
		response = self.read()
		return response


