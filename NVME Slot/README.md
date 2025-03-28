# NVME Slot on HackberryPi_CM5

There is an NVME Slot on board which is only compatible with 2242 ssd or hailo 8 AI accelerator card.
![image](https://github.com/user-attachments/assets/70425743-f175-4eb6-a6be-5a03c525eecf)
There are many types of ssd that are not compatible with RaspberryPi, it is recommended to buy the ssd directly from shop of elecrow:


## Use SSD with HackberryPi_CM5

First enable PCIe Interface, note: PCIE interface is enabled on the PI5B by default.
If the PCIE interface is not enabled, you add the following content in "/boot/firmware/config.txt" by typing ```sudo nano /boot/firmware/config.txt``` in a terminal:
```sh
dtparam=pciex1
```
at [all] section

The default mode of PCIe is gen2. If you need to enable PCIe Gen3, you need to add the following content at /boot/firmware/config.txt:
```sh
dtparam=pciex1_gen=3
```
at [all] section
