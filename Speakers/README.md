# Speakers on HackberryPi_CM5

As we know, it's always been somehow difficult or tricky to add sound for RaspberryPi. Some use gpio to generate pwm to make sound for speakers, some use I2S audio module to generate sound for speakers. But they all have some shortcomings. PWM generated from gpios on raspberryPi have much noise that make the speakers nealy usable, and I2S audio module will occupy the very precious gpio resoureces(usually take 3 gpio pins). And in some operating system there is no driver for these pwm or I2S audio module. Due to the reasons above this is how I solve the sound problem.

## Bluetooth speakers on board

This is how I add sound on HackberryPi_CM5: Integrating a bluetooth speaker on board.

The solution is bluetooth audio module + Stereo Speaker amplifier
![image](https://github.com/user-attachments/assets/fa1b662a-e1b8-4add-a23a-1842e9664163)
The bluetooth audio module is very easy to source, it's called MH-M18.

The amplifier is a very classic type called PAM8406.
