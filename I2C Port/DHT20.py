
import time
import smbus2

address = 0x38  # DHT20 I2C address

# Initialize the I2C bus (usually bus 1 on Raspberry Pi)
i2cbus = smbus2.SMBus(11)
time.sleep(0.5)  # Allow sensor to power up

while True:
    # Read a status byte to check initialization
    data = i2cbus.read_i2c_block_data(address, 0x71, 1)
    if (data[0] | 0x08) == 0:
        print('Initialization error')
    else:
        # Trigger a measurement by writing the command
        i2cbus.write_i2c_block_data(address, 0xac, [0x33, 0x00])
        time.sleep(0.1)  # Give sensor time to perform measurement

        # Read 7 bytes of data from the sensor
        data = i2cbus.read_i2c_block_data(address, 0x71, 7)

        # Calculate raw temperature and convert to °C
        Traw = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
        temperature = 200 * float(Traw) / (2**20) - 50

        # Calculate raw humidity and convert to %RH
        Hraw = ((data[3] & 0xF0) >> 4) | (data[1] << 12) | (data[2] << 4)
        humidity = 100 * float(Hraw) / (2**20)

        print("Temperature: {:.2f}°C, Humidity: {:.2f}%".format(temperature, humidity))

    # Wait for 1 second before the next reading
    time.sleep(1)
