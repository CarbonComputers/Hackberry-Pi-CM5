# RTC_Battery on HackberryPi_CM5

The battery type on HackberryPi_CM5 is CR927 battery

This page tells you how to install the battery

After you install the battery you can check the battery voltage first by typing this in terminal:

```sh
cat /sys/devices/platform/soc/soc:rpi_rtc/rtc/rtc0/battery_voltage
```
