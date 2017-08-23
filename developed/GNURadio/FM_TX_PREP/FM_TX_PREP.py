#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM TX PREP
# Author: FTG
# Description: Prepares file for FM transmission.
# Generated: Mon Aug 21 06:37:59 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class FM_TX_PREP(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "FM TX PREP")

        ##################################################
        # Variables
        ##################################################
        self.audio_rate = audio_rate = 384000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=10,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/media/usb/radio/input.wav', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/debian/output.raw', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate,
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_file_sink_0, 0))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate


def main(top_block_cls=FM_TX_PREP, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
