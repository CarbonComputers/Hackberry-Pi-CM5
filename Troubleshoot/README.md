# Troubleshoot of HackberryPi_CM5

### HackberryPi_CM5 can't wake up after I shut it down

Because the power source +5V of HackberryPi_CM5 is generated from the Power Bank SOC IP5310, one character of this chip is that it has small current detect function which means once the load is too small for example under 50-80ma, the power source +5V will automatically be cut up by IP5310. Once the pi is shut down, it consumes too less power that the main power source +5V will be cut down by IP5310. There is one solution to avoid by plugging a small adapter dongle board. check this:

### Keyboard has no reaction

Once you find the keyboard of HackberryPi_CM5 can't type and the trackpad has no reaction to mouse sweep. First check if the left red switch is on the right position. More information about the switch can be found in this page. If the keyboard is at the right position, maybe the keyborad is set into bootloader mode manually. Check if the is one U-Disk found by the pi at desktop. If there is, just reboot the device and the keyborad can get back into function.

### Trackpad no reaction to mouse sweep

When you troubleshoot the second situation and still found the trackpad has no reaction to your finger, try to reboot first and see if the trackpad comes back. If not, please contact me

### There are lines on the screen

Maybe after you boot the device up and found the display showing some lines as the picture shows below, don't worry that you may have broken the display. This is an effect called display polarized, it always happens when the display driver chip is powered on while there is no display image input, you can first disable the power saving or screensaving function in your operating system and put the device running like one hour and the display can revocer itsself.

### HackberryPi_CM5 won't boot.

You may find that the device won't boot up after some usage. There is one status LED showing the current status on top of the HackberryPi_CM5. If the white LED won't blink after you blink, that means the kernel image might break down. You need to flash a new image into the tf card or the tf card is broken and you need to use another new card.

### No sound 

The speakers are controlled by a bluetooth audio module and it's so you can pair with the audio module via bluetooth. But in some operating system you need to connect the pi with the module maunally after you pair with it. 

