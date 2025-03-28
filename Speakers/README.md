# Speakers on HackberryPi_CM5

As we know, it's always been somehow difficult or tricky to add sound for RaspberryPi. Some use gpio to generate pwm to make sound for speakers, some use I2S audio module to generate sound for speakers. But they all have some shortcomings. PWM generated from gpios on raspberryPi have much noise that make the speakers nealy usable, and I2S audio module will occupy the very precious gpio resoureces(usually take 3 gpio pins). And in some operating system there is no driver for these pwm or I2S audio module. Due to the reasons above this is how I solve the sound problem.

## Bluetooth speakers on board

This is how I add sound on HackberryPi_CM5: Integrating a bluetooth speaker on board.  


**Advantages**:  
**No gpio needed**: The SBC communicates with the audio module via bluetooth so there is no gpio needed.  
**Driverless**: As long as your operating system installed have bluetooth driver, you can pair with the speaker and no external driver needed.  
**Good sound quality**: The 
**Cheap cost**: compared with some USB solution, the bluetooth audio module is moch more cheaper.  


The solution is bluetooth audio module + Stereo Speaker amplifier  
![image](https://github.com/user-attachments/assets/fa1b662a-e1b8-4add-a23a-1842e9664163)  
The bluetooth audio module is very easy to source, it's called MH-M18.  
![d8e22f566b35eec8c523338b65ded325](https://github.com/user-attachments/assets/870e180d-ea77-4786-b0f6-767c084fa577)  
The amplifier is a very classic type called PAM8406.  
![image](https://github.com/user-attachments/assets/2b6e1704-28a0-40e7-b78f-e65098a3e902)  

# Speakers

There are two types of speakers used on HackberryPi_CM5. 1507 speaker for Q20 version and 1511 speaker for Q10 and 9900 version. They are both 8Ω speakers and have difference at the dimension. You can find the datasheet about the speakers in this page.
