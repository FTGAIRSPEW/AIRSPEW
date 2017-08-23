# AIRSPEW
AirSpew: Modular Information Dissemination System

GNU Radio Scripts 

This folder contains the two GNU Radio scripts that were used in the Radio module.
Both folders contain the GNU Radio Companion design file and the resulting Python script.

FM_TX_PREP – This script pre-processes the input sound file by modulating it for wide-band FM transmission and also resampling to match the HackRF One’s minimum sampling frequency (4 MHz). It looks for a 384 KHz 32-bit float PCM WAV file named input.wav in the USB drive’s radio directory and outputs a re-sampled modulated intermediate file ready for transmission to a temporary location onboard the processing unit.

FM_TX – This script perform the actual FM transmission, it reads in the intermediate file and feeds it to the HackRF One for transmission. This script also controls the transmission parameters such as the power levels and transmission frequency (96.1 MHz FM).