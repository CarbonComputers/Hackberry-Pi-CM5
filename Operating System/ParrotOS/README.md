# Install ParrotOS on HackberryPi_CM5

### Parrot OS is a Linux distribution based on Debian with a focus on security, privacy, and development.

```Step1``` Download the Image for RaspberryPi on this [page](https://parrotsec.org/download/)  
```Step2``` Flash the downloaded image into a TF card  
```Step3``` Copy the following content into the config.txt and override  
```Step4``` Insert the TF card into the HackberryPi_CM5 and power it on, wait a few seconds and you can see it booting  



```sh
# For more options and information see
# http://rptl.io/configtxt
# Some settings may impact device functionality. See link above for details

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
#dtparam=spi=on

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Additional overlays and parameters are documented
# /boot/firmware/overlays/README

# Automatically load overlays for detected cameras
camera_auto_detect=1

# Automatically load overlays for detected DSI displays
display_auto_detect=1

# Automatically load initramfs files, if found
auto_initramfs=1

# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d
max_framebuffers=2

# Don't have the firmware create an initial video= setting in cmdline.txt.
# Use the kernel's default instead.
disable_fw_kms_setup=1

# Run in 64-bit mode
arm_64bit=1

# Disable compensation for displays with overscan
disable_overscan=1

# Run as fast as firmware / board allows
arm_boost=1

[cm4]
# Enable host mode on the 2711 built-in XHCI USB controller.
# This line should be removed if the legacy DWC2 controller is required
# (e.g. for USB device mode) or if USB support is not required.
otg_mode=1

[all]
dtoverlay=dwc2,dr_mode=host
dtoverlay=vc4-kms-v3d
dtoverlay=vc4-kms-dpi-hyperpixel4sq

```

You can type ```startx``` in terminal to enter desktop environment

![image](https://github.com/user-attachments/assets/c2be8186-bf20-4923-9fe9-21f9eb4ba194)
