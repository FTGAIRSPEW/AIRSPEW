#!/bin/sh

# Make sure LED3 is off to indicate we are getting system ready
echo 0 > /sys/class/leds/beaglebone\:green\:usr3/brightness

# Log the time
date

# Let the board settle down for 20 seconds
# TODO: Future optimization: get status instead of blind sleep
sleep 20

# Mount the SD card
mount /dev/sda1 /media/usb/

# Configure the IO pin
echo in > /sys/class/gpio/gpio60/direction

# Detemine the operation  mode
mode=`cat /media/usb/mode.txt`

# Set the environment if in radio mode
if [ $mode = radio ]
then

	export PATH="/home/debian/prefix/default/bin:$PATH"
	export PYTHONPATH="/home/debian/prefix/default/python:/home/debian/prefix/default/lib/python2.6/site-packages:/home/debian/prefix/default/lib64/python2.6/site-packages:/home/debian/prefix/default/lib/python2.6/dist-packages:/home/debian/prefix/default/lib64/python2.6/dist-packages:/home/debian/prefix/default/lib/python2.7/site-packages:/home/debian/prefix/default/lib64/python2.7/site-packages:/home/debian/prefix/default/lib/python2.7/dist-packages:/home/debian/prefix/default/lib64/python2.7/dist-packages:$PYTHONPATH"
	export LD_LIBRARY_PATH="/home/debian/prefix/default/lib:/home/debian/prefix/default/lib64/:$LD_LIBRARY_PATH"
	export LIBRARY_PATH="/home/debian/prefix/default/lib:/home/debian/prefix/default/lib64/:$LIBRARY_PATH"
	export PKG_CONFIG_PATH="/home/debian/prefix/default/lib/pkgconfig:/home/debian/prefix/default/lib64/pkgconfig:$PKG_CONFIG_PATH"
	export PYBOMBS_PREFIX="/home/debian/prefix/default"
	# If we're in a Python virtualenv, activate that
	if [ -r /home/debian/prefix/default/bin/activate ]; then
	    source /home/debian/prefix/default/bin/activate
	fi

	echo Preparing File for Radio...
	# TODO: Future optimization: hash input files and compare if prep work is needed
	/usr/bin/python2 -u /home/debian/GNURadio_Scripts/FM_TX_PREP/FM_TX_PREP.py
fi

# Turn on LED3 to let user know the system is ready
echo System is Ready...
echo 1 > /sys/class/leds/beaglebone\:green\:usr3/brightness

# Wait until the LED is active
while [ True ]
do
	# Read current value of IO pin
	value=`cat /sys/class/gpio/gpio60/value`
	# If true then perform the action
	if [ $value = 1 ]
	#if [ 1 ]
	then
		# Based on mode perform the desired function
		if [ $mode = speaker ]
		then
			echo SPEAKER MODE
			# Play the file for speaker playback
			aplay /media/usb/speaker/*.wav
		elif [ $mode = radio ]
		then
			echo RADIO MODE
			# Send the FM message
			/usr/bin/python2 -u /home/debian/GNURadio_Scripts/FM_TX/FM_TX.py
		elif [ $mode = drop ]
		then
			echo DROP MODE
			# Execute the servo control script
			python /home/debian/servo.py
		fi
	fi
	#Sleep for five second
	sleep 5
done
