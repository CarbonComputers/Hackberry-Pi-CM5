# Troubleshoot of HackberryPi_CM5

### Keyboard has no reaction

Once you find the keyboard of HackberryPi_CM5 can't type and the trackpad has no reaction to mouse sweep. First check if the left red switch is on the right position. More information about the switch can be found in this page. If the keyboard is at the right position, maybe the keyborad is set into bootloader mode manually. Check if the is one U-Disk found by the pi at desktop. If there is, just reboot the device and the keyborad can get back into function.

### Trackpad no reaction to mouse sweep

When you troubleshoot the second situation and still found the trackpad has no reaction to your finger, try to reboot first and see if the trackpad comes back. If not, please contact me

### There are lines on the screen

Maybe after you boot the device up and found the display showing some lines as the picture shows below, don't worry that you may have broken the display. This is an effect called display polarized, it always happens when the display driver chip is powered on while there is no display image input, you can first disable the power saving or screensaving function in your operating system and put the device running like one hour and the display can revocer itsself.

### HackberryPi_CM5 won't boot(black screen).

1. Boot with TF card: You may find that the device won't boot up after some usage. There is one status LED showing the current status on top of the HackberryPi_CM5. If the white LED won't blink after you blink, that means the kernel image might break down. You need to flash a new image into the tf card or the tf card is broken and you need to use another new card.
2. Boot with SSD: Make sure that the image is stored at the p1 partition(like nvme0n1p1 not nvme0n1p2), otherwise there is a chance that the device can't boot with the image at p2

### No sound 

The speakers are controlled by a bluetooth audio module and it's so you can pair with the audio module via bluetooth. But in some operating system you need to connect the pi with the module maunally after you pair with it. 

