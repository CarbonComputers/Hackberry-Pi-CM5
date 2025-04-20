# Install Kali on HackberryPi_CM5

### Kali Linux is a Linux distribution designed for digital forensics and penetration testing. It is maintained and funded by Offensive Security.

```Step1```Download and install the kali image from pi imager into a tf card```Main Menu-> other specfic purpose os->kali linux```
```Step2``` Copy the following content into the config.txt and override  
```Step3``` Insert the TF card into the HackberryPi_CM5 and power it on, wait a few seconds and you can see it booting  

Compared with other operating system, it's just needed to delete the vms, because the .... is currently not likely to be supported in kali os.


```sh



```

⚠️ **Note:**  

Bluetooth may not be enabled by default in Kali on current version of Kali. You need to enable it manually, here are the steps:

```sh
sudo apt install bluetooth
```
and then
```sh
sudo systemcli enable bluetooth.service
```
Then you can connect with the speakers and use bluetooth on HackberryPi_CM5 in Kali
