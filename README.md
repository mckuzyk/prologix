# prologix

This package is a wrapper for the Prologix GPIB to usb that provides a simple
interface for writing to, reading from, and querying instruemnts.

### Required packages

* pySerial

### Usage

Creat a communication line with an instrument through the prologix adapter.
First open a line of communication with the prologix class, and then add
instruments.  A typical example would be

```python

# Create a prologix object 
plx = prologix.Prologix(port='COM3', baud=9600, timeout=3)

# Creat a new instrument representing an oscilloscope at gpib address 5
scope = plx.open_instrument(gpib_address = 5)

# Query the oscilloscope with the message *IDN? to ask what model the scope is
scope.query('*IDN?')

```
