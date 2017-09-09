#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM TX
# Author: FTG
# Description: Transmits FM from intermediate file
# Generated: Mon Aug 21 05:34:46 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import pmt
import time


class FM_TX(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "FM TX")

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(4000000)
        self.osmosdr_sink_0.set_center_freq(96100000, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(16, 0)
        self.osmosdr_sink_0.set_if_gain(16, 0)
        self.osmosdr_sink_0.set_bb_gain(16, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/debian/output.raw', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.osmosdr_sink_0, 0))


def main(top_block_cls=FM_TX, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
