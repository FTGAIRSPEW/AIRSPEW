# AIRSPEW
AirSpew: Modular Information Dissemination System

Linux Service

This folder contains the Linux service scripts that were used for all three modules.

airspew_run.sh – This script is the runner script and simply elevates execution level and logs the output of stand/error to a log file for troubleshooting purposes. This script was installed as a service on the processing unit’s operating system (Debian distribution of Linux).

airspew.sh – This is the main service script, it is executed by the runner script and performs the control logic for all three modules. The flow process includes:
* Board preparation (PIN settings, USB drive mounting, and mode determination)
* Configuring the GNU Radio system environment and preprocessing of the audio file for the Radio mode
* Based on the mode specified by the user (using the mode.txt file in the USB drive) perform the desired function once the payload is activated via the drone's LED:
  * Speaker – plays the audio file located on the USB drive’s speaker folder (any file name), most audio formats supported; it has been tested with a 44.1 KHz 32-bit float PCM WAV file
  * Radio – broadcasts the WAV file located on the USB drive’s radio folder, formatted as 384 KHz 32-bit float PCM WAV and named input.wav
  *Drop- activates the leaflet drop mechanism by controlling the servo that holds the papers in place
