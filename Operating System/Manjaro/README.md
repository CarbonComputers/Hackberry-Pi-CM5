# Install Manjaro on HackberryPi_CM5

### Manjaro is a free and open-source Linux distribution based on the Arch Linux operating system that has a focus on user-friendliness and accessibility. 

```Step1```  Download the Release Image for RaspberryPi on this [page](https://github.com/manjaro-arm/rpi4-images/releases). Although it's labeled as pi4, you can still install the OS on pi5 and should run without issue. For example we can choose Manjaro with plasma desktop  
![image](https://github.com/user-attachments/assets/77511ebb-c6fc-4556-9b0b-dbe8d535705a)  
```Step2``` Flash the downloaded image into a TF card  
```Step3``` Copy the following content into the config.txt and override  
```Step4``` Insert the TF card into the HackberryPi_CM5 and power it on, wait a few seconds and you can see it booting  

```sh
# See /boot/overlays/README for all available options

# Uncomment some or all of these to enable optional Hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Run in 64bit mode
arm_64bit=1

# Auto load correct initramfs files if found
auto_initramfs=1

# Run as fast as the firmware/board allows
arm_boost=1

# Disable compensation for displays with overscan
disable_overscan=1

# Enable sound
dtparam=audio=on
# Uncomment if no sound thru hdmi
#hdmi_drive=2

# Auto load overlays for detected cameras
camera_auto_detect=1
# Auto load overlays for detected DSI displays
display_auto_detect=1

# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
# For pi4's and above boards uncomment next line & Comment out above line
#dtoverlay=vc4-kms-v3d,cma-512
max_framebuffers=2

# Don't have the firmware create an initial video= setting in cmdline.txt
# Use the kernel default instead
#disable_fw_kms_setup=1

# Disable rainbow screen at boot
disable_splash=1

# RPi 5B/4B/400 ONLY
# For 4k content @ 60 Hz refresh rate, uncomment hdmi_enable_4kp60=1
#hdmi_enable_4kp60=1
# If video breaks with hdmi_enable_4kp60=1 uncomment
#force_turbo=1


[cm4]
# Enable host mode on the 2711 built-in XHCI USB controller
# This line should be remoed if the legacy DWC2 controller is required
otg_mode=1

[cm5]
dtoverlay=dwc2,dr_mode=host

[all]
dtoverlay=dwc2,dr_mode=host
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq
```
![f6f5cfc7bf51e22420ad9562048b33e](https://github.com/user-attachments/assets/50c78d32-e169-4337-be83-55a8846ea0a2)

If you found that Wifi won't work add the following into the cmdline.txt

```sh
brcmfmac.roamoff=1 brcmfmac.feature_disable=0x282000
```sh

⚠️   
### Note: It seems by default the image on screen is set at 275% scale. You might need to connect to an external HDMI display to reset the scale on Manjaro
