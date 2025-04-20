# RTC_Battery on HackberryPi_CM5

There is an RTC battery on board on HackberryPi_CM5 and is pre-installed before delivery

![image](https://github.com/user-attachments/assets/f9ec7797-bb5f-4f07-8b85-8a5f66d573b0)


You can check the battery voltage first by typing this in terminal:

```sh
cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/battery_voltage
```
![image](https://github.com/user-attachments/assets/2b21954b-3a8b-4bb2-adc6-bddab41c39dc)

A new battery voltage should be around 3.3V, so it read should be approximately 3300000
