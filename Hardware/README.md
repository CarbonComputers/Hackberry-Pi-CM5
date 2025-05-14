# The key hardware design features of the HackberryPi_CM5

* DPI display circuit: 40-pin Connector+Display backlight boost circuit: 3.3V->12V
* Bluetooth speaker on board: Basically driverless between different operating system
* Powersource: Powerbank SOC IP5310 provide 5V power + IP5306 for charging
* Keyboard: Keyboard controller RP2040 and communicates with CM5 via USB interface
* CM5 Slots: 2 x DF40C-100DS-0.4V(51)
* Push-push out TF card Slot: quick change between different tf cards
* 2 x USB 3.0 Ports: Use with high speed U-Disk
* M.2 Slot on board: Boot on SSD or use with AI Kit
* USB-KVM circuit for Keyboard: Make the device as emergency keyboard
* Full size HDMI Port: No longer need for mini hdmi adapter!
* Stemma QT port: Connect with I2C sensors
* Battery voltage measure chip on board: Get the current battery voltage
* Reserved fan connector

# BOM file of HackberryPi_CM5

Check the [ibom file](https://github.com/ZitaoTech/HackberryPiCM5/blob/main/Hardware/Bom_HackberryPi_CM5_Q20_rev0.html) of this page to review the component on HackberryPi_CM5
![image](https://github.com/user-attachments/assets/9dc0ef23-dd5d-40aa-aba6-14b0ed139410)
