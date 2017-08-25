
# AIRSPEW
AirSpew: Modular Information Dissemination System

## Radio Module
Using a computer access the blue USB drive and edit the mode.txt file to indicate radio mode by typing “radio” into the file. Save the desired message for broadcast under the “radio” folder, it must be named “input.wav” and be a 384 KHz 32-bit float PCM WAV file. Insert the USB drive back into the 4 port USB hub on the drone.

For the radio module attach the panel with the large speaker to the bottom of the drone, secure with zip-ties:

![FTG AirSpew Logo](/media/pictures/Radio_Side.jpg)

Attach the HackRF One module onto the panel, also using zip-ties:

![FTG AirSpew Logo](/media/pictures/Radio_Top.jpg)

Connect the USB cable from the HackRF One module to the 4 port USB hub on the processing node:

![FTG AirSpew Logo](/media/pictures/Radio-PU.jpg)

Power on the drone’s controller and drone and wait for system checks to complete. Using the configured button check that you are able to turn on/off the drone’s LED’s – check the LED opposite of the one covered.

Plug in the processing units USB cable into the battery and turn on the battery/speaker:

![FTG AirSpew Logo](/media/pictures/Radio_Side_B.jpg)

Wait until the blue LED closes to the Ethernet header (one of four LEDs) on the processing unit is on; this indicates that the processing unit and drop module have been initialized properly - this should take approximately one minute after connecting the battery, for this module the boot time depends on the length of the audio input file.

Fly the drone to the desired location and start the broadcast by pressing the LED control button on the drone’s remote – the broadcast will be heard on 96.1FM:

*Click to Play Video*

[![Alt text](https://img.youtube.com/vi/qCI9H9dysWo/0.jpg)](https://www.youtube.com/watch?v=qCI9H9dysWo)
