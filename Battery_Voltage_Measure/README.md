# Battery voltage measure on HackberryPi_CM5

There is a microchip on board that can measure the current battery voltage called MAX17048.

It communicates with the CM5 via I2C interface  

With the simple python code below the HackberryPi_CM5 can measure the current battery voltage for example in thonny  
```sh
import smbus2
import time

class MAX17048:
    def __init__(self, i2c_bus=11, i2c_address=0x36):
        self.bus = smbus2.SMBus(i2c_bus)
        self.address = i2c_address

    def read_voltage(self):
        try:
            # Read voltage registers (0x02 and 0x03)
            read = self.bus.read_i2c_block_data(self.address, 0x02, 2)
            
            # Combine the bytes and convert to voltage
            voltage_raw = (read[0] << 8) | read[1]
            voltage = voltage_raw * 0.078125  # 78.125μV per LSB
            
            return voltage / 1000  # Convert to volts
            
        except Exception as e:
            print(f"Error reading voltage: {e}")
            return None

    def close(self):
        self.bus.close()

if __name__ == "__main__":
    max17048 = MAX17048()
    
    try:
        while True:
            voltage = max17048.read_voltage()
            if voltage is not None:
                print(f"Battery Voltage: {voltage:.2f} V")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram stopped")
        max17048.close()
```

![image](https://github.com/user-attachments/assets/55db79cd-ad6f-4a8d-9a4a-d0ffe60f7829)

# Hardware

This is the schematic of the battery voltage measure part on HackberryPi_CM5  

![image](https://github.com/user-attachments/assets/a7473953-f248-4109-9d9c-d08dfec1d01e)  

The battery voltage measure chip and the screen’s touch controller are on the same I2C bus on HackberryPi_CM5.


