# External antenna on HackberryPi_CM5

In my experiments, the signal from the PCB antenna on the Raspberry Pi CM5 module may not be ideal when a passive aluminum heatsink is installed. Therefore, adding an external antenna can sometimes enhance the signal strength of the CM5.
The following are the installation steps:

### Install external antenna on HackberryPi_CM5

```Step1:``` Loosen the four screws on the back panel.  
```Step2:``` Connect the external FPC antenna with a first-generation IPEX connector to the antenna socket on the Raspberry Pi CM5 board.  
```Step3:``` Adjust the direction of the antenna to prevent interference with the enclosure, as shown in the picture:  
```Step4:``` Add a line of code in the config.txt file by 
```sh
sudo nano /boot/firmware/config.txt
```

with the following line
```sh
dtparam=ant2
```
Source: [CM5 datasheet](https://datasheets.raspberrypi.com/cm5/cm5-datasheet.pdf)  
Now you can have a better signal experience.

![image](https://github.com/user-attachments/assets/6dc40a4f-95d1-45e1-93eb-f02bfad4a5b9)

#### You can buy the external antenna with HackberryPi_CM5 together on elecrow:  
[Buy from elecrow](https://www.elecrow.com/external-fpc-antenna-for-hackberrypi-cm5.html)
