# AIRSPEW
AirSpew: Modular Information Dissemination System

## Design Details
### Overview

FTG’s submission to AirSpew consists of a modular design that achieves the three objectives: pamphlet drop, speaker broadcast audio, and FM transmission. The design consists of a base processing unit shared among the three modes along with mode specific hardware. Browse to the directories specified above to learn more about the design and operation.

* base processing unit:
  * BeagleBone Black development platform - provides Linux based processing unit that controls all three modes of operation
  * 4 port USB hub - expands the number of available USB ports
  * USB thumbdrive - contains the user configurable mode setting along with media files for speaker and radio mode
  * custom LED detection hardware - non-intrusive interface to drone platform to allow for payload activation via drone’s remote controllable LED
  * mounting hardware - various mounting components to facilitate module operation
  
![HW Overview](/media/pictures/HW_Overview.PNG)  

* drop module
  * paper tray – holds leaflet payload
  * USB battery – provides power to the base processing unit
  * servo motor – acts as the leaflet release mechanism
  * servo connector – provide 5 V power to servo and signal cable to processing unit to activate servo


![Drop Overview](/media/pictures/Drop_Overview.PNG)

* speaker module
 * speaker and USB battery combination – provides the audio dissemination and power to the base processing unit
 * Mini HDMI to VGA/audio connector – provides the audio out connection from the processing unit


![Speaker Overview](/media/pictures/Speaker_Overview.PNG)

* radio module
  * speaker and USB battery combination – provides the power to the base processing unit
  * HackRF One transceiver – provides the transmit/receive radio functionality
  * HackRF One antenna – multipurpose antenna 
  * USB data/power – connects HackRF to the BeagleBone processing unit for power and data

![Speaker Overview](/media/pictures/Radio_Overview.PNG)

