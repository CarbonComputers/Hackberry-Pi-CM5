# NVME Slot on HackberryPi_CM5

There is an NVME Slot on board which is only compatible with 2242 ssd or hailo 8 AI accelerator card.
![image](https://github.com/user-attachments/assets/70425743-f175-4eb6-a6be-5a03c525eecf)
There are many types of ssd that are not compatible with RaspberryPi, it is recommended to buy the ssd directly from shop of elecrow:


## Use SSD with HackberryPi_CM5

### Enable PCIe
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

Now the ```config.txt``` file will look like this:  
![image](https://github.com/user-attachments/assets/4eaf41f2-989e-48ca-8308-74255f591d27)

Now make a ```sudo reboot``` and type ```lsblk``` The SSD should be recognized by the Pi:
![image](https://github.com/user-attachments/assets/da639e70-392c-4627-a9c4-45de4356bc23)

### Partition
```sh
sudo fdisk /dev/nvme0n1
```
Execute n to add the partition, and then just type enter enter enter until a new partition is created, and then execute w to save and exit.
![3e1775b2937b64a7e02af512a7da948c](https://github.com/user-attachments/assets/efba3dd9-927c-44ab-b508-64ea986d3372)

### Format
```sh
sudo mkfs.ext4 /dev/nvme0n1p1
```
Wait for a few moments, when done has appeared, it means that the formatting has been carried out.
![1a0374a7-da44-4201-9268-f5ef6763b0c1](https://github.com/user-attachments/assets/59d68cfb-bc9b-4627-8ab2-7d934cb8fa68)

### Mount
Create Mount Directory(Use any name)
```sh
sudo mkdir ssd
```
Mount the device
```sh
sudo mount /dev/nvme0n1p1 ./ssd
```
