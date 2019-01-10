# prologix

This package is a wrapper for the Prologix GPIB to usb that provides a simple
interface for writing to, reading from, and querying instruemnts.

### Required packages

* pySerial

### Usage

Creat a communication line with an instrument by creating an instance of the
prologix class.  A typical example would be

```python

# Create a communication line to an oscilloscope at GPIB address 5
scope = prologix.prologix(gpib=5, port='COM3', baud=9600, timeout=3)

# Query the oscilloscope with the message *IDN? to ask what model the scope is
scope.query('*IDN?')

```
