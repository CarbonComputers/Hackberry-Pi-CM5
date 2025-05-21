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

# How to use the .vil file?  
Let's say that you changed many keycodes and want to reset the keyboard layout  
First download vial app from [vial](https://get.vial.today/) homepage![image](https://github.com/user-attachments/assets/351fe201-cb4a-4483-83c8-f314ae1b860c)  
Install the vial app and open the app  
Then connect yor computer with Hackberry and in menu **file**->**Load saved layout** and select the .vil file, the keyboard layout will be reset.  

# Default Layout and Layers
### Layer0:
![Keymap_Layer0](https://github.com/user-attachments/assets/85eecbcd-65fe-4cdd-a51c-9182c82d6bc5)

### Layer 1:
![Keymap_Layer1](https://github.com/user-attachments/assets/28c5043a-dd23-416b-a23b-b14b5fdf9ce6)

### Layer 2:
![Keymap_Layer2](https://github.com/user-attachments/assets/221d4d2e-35c9-4349-9c26-a69c27b6d6a1)

# Customize the keymap

Thanks to the qmk firmware running on the keyboard, each key on HackberryPi_CM5 can be remapped on [vial app](https://get.vial.today/), just need to connect the HackberryPi with another computer via the usbc port below and flip the left switch and the keyboard output will be changed and the computer will recognize the keyboard on vial app. 

# Some features you can use in via app

### Tap dance
You can set each key on the keyboard on each layer to trigger some keycode with single tap, double tap or hold in tapdance
![image](https://github.com/user-attachments/assets/9abfda2b-e50f-4dd1-bb3b-b38e9443e5ee)
![image](https://github.com/user-attachments/assets/906d2bc7-08cd-4536-8c16-bde581c5c4db)
### Macros
You can use record function in vial app and output a lot of text using macros function
![image](https://github.com/user-attachments/assets/791de464-f01c-4d54-8314-c62dc13d63ad)
For more information please refer to the user manual on [vial page](https://get.vial.today/manual/)



