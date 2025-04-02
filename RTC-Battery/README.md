# RTC_Battery on HackberryPi_CM5

The battery type on HackberryPi_CM5 is CR927 battery

This page tells you how to install the battery

After you install the battery you can check the battery voltage first by typing this in terminal:

```sh
cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/battery_voltage
```
![image](https://github.com/user-attachments/assets/2b21954b-3a8b-4bb2-adc6-bddab41c39dc)

A new battery voltage should be around 3.3V, so it read should be approximately 3300000
