# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# STS21
# This code is designed to work with the STS21_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Temperature?sku=STS21_I2CS#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# STS21 address, 0x4A(74)
# Select Command
#		0xF3(243)	Temperature measurement in NO HOLD mode
bus.write_byte(0x4A, 0xF3)

time.sleep(0.5)

# STS21 address, 0x4A(74)
# Read data back, 2 bytes, MSB first
data0 = bus.read_byte(0x4A)
data1 = bus.read_byte(0x4A)

# Convert the data
temp = (data0 * 256 + data1) & 0xFFFC
cTemp = -46.85 + (175.72 * temp / 65536.0)
fTemp = cTemp * 1.8 + 32

# Output data to screen
print "Temperature in Celsius is :  %.2f C" %cTemp
print "Temperature in Fahrenheit is :  %.2f F" %fTemp
