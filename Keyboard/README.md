# Keyboard on HackberryPi_CM5

There are currently 3 versions of keyboards for HackberryPi_CM5: Q10 Q20 and 9900 keyboards

Different keyboard has its own style

* Q10: Q10 keyboard has linear layout and the keycap is slightly smaller than the Q20, the original Q10 keyboard has no top row keys and trackpad, I use the trackpad from 9900 and add another top row keys with PS game controller icon on it.
* Q20: Q20 keyboard has linear layout and has the largest keycap, but there the trackpad on Q20 keyboard is the smallest and it has no backlight around the trackpad.
* 9900: 9900 keyboard has ergonomic smile layout, the keycap is the smallest one. 

# Keyboard function on HackberryPi_CM5

Each keyboard has the same keycap number and the trackpad can be used as mouse and also scroll wheel when capslock is enabled, when capslock is enabled the trackpad backlight on Q10 and 9900 will be lighted on while on Q20 the top row keys backlight will be lighted on.

Each keyboard backlight can be adjusted with 10 steps.

When hold Ctrl, mouse dpi /2 and while hold Alt, mouse dpix2.

# Keyboard firmware

The keyboard controller on HackberryPi_CM5 is RP2040 chip and the firmware on it is qmk firmware.


# Customize the keymap

Thanks to the qmk firmware running on the keyboard, each key on HackberryPi_CM5 can be remapped on [vial app](https://get.vial.today/), just need to connect the HackberryPi with another computer via the usbc port below and flip the left switch and the keyboard output will be changed and the computer will recognize the keyboard on vial app. 
