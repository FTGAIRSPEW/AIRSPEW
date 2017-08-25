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
* For most of the connections between the module components and the drone are completed with zip-ties, we recommend reusable zip ties because they can be easily released and re-used

All modules use the processing unit; as such it should be mounted first on the drone:
![FTG AirSpew Logo](/media/pictures/PU-Front.jpg)
![FTG AirSpew Logo](/media/pictures/PU-LED.jpg)
![FTG AirSpew Logo](/media/pictures/PU-UpsideDown.jpg)
