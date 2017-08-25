
# AIRSPEW
AirSpew: Modular Information Dissemination System

## Operation Details

### Important Notes:
* During testing best response was found using DJI's Atti flight mode - this is our recommended flight mode when the modules are attached
* When using the included LED signal kit in an outdoor setting with a lot of natural light it is recommended to cover the outside of the chosen LED with electrical tape to reduce the chance of a false trigger. The prototype consists of a blacked out LED cover, future plan would be to make this piece out of plastic
* The GNU Radio tranmission software was inadvertely shipped with power level configuration that  will not allow it to run on battery and perform the FM transmission. The module can be tested using the supplied wall power supply, the power configuration can also be adjusted to allow transmission on battery
* Complete drone startup and checks before turning the main processing unit to reduce module trigger during drone startup sequence

### Preparation
In order to prepare for flight the battery associated with the module should be charged completely. 
* The speaker/battery combination for use in the speaker and radio modules has a “battery” check button on the rear (close to the AUX IN)
* The smaller battery used on the drop module has a button on top to check charge level

For most of the connections between the module components and the drone are completed with zip-ties, we recommend reusable zip ties because they can be easily released and re-used

One of the drone’s controller’s channel buttons must be configured to turn on/off the rear LEDs, this will be used as the trigger to active the payloads

All modules use the processing unit; as such it should be mounted first on the drone:
![FTG AirSpew Logo](/media/pictures/PU-Front.jpg)
![FTG AirSpew Logo](/media/pictures/PU-LED.jpg)
![FTG AirSpew Logo](/media/pictures/PU-UpsideDown.jpg)

### Drop Module
For the drop module attach the tray with the opening towards the front of the drone with 3 plastic ties on each side:
![FTG AirSpew Logo](/media/pictures/Drop-Side-A.jpg)

Attach the servo’s USB cable to the 4 port USB hub and attach the processing unit’s single servo signal cable (black cable, loose end was inserted into styrofoam block for protection) to the servo’s signal cable (the only populated pin in the servo’s header):
![FTG AirSpew Logo](/media/pictures/Drop-to-PU.jpg)
![FTG AirSpew Logo](/media/pictures/Drop_Connection.jpg)

Power on the drone’s controller and drone and wait for system checks to complete. Using the configured button check that you are able to turn on/off the drone’s LED’s – check the LED opposite of the one covered.

Plug in the processing units USB cable into the battery that resides in top of the paper tray.

Wait until the blue LED closes to the Ethernet header (one of four LEDs) on the processing unit is on; this indicates that the processing unit and drop module have been initialized properly - this should take approximately 30 seconds after connecting the battery:
![FTG AirSpew Logo](/media/pictures/Ready-LED.jpg)

Lift the servo’s arm and load the paper into the tray. Fly the drone to the desired location and release the pamphlets by pressing the LED control button on the drone’s remote – the servo will activate lifting its arm and the pamphlets will be distributed :
