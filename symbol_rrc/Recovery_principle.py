#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Recovery Principle
# Generated: Mon Oct 22 22:28:38 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class Recovery_principle(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Recovery Principle")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Recovery Principle")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Recovery_principle")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.ntaps = ntaps = 45
        self.nfilts = nfilts = 32
        self.excess_bw = excess_bw = 0.35
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.time_offset = time_offset = 1.00
        self.taps = taps = [1.0 + 0.0j, ]
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 45*nfilts)
        self.rrc_rx = rrc_rx = firdes.root_raised_cosine(1.0, sps, 1, excess_bw, ntaps)
        self.qpsk = qpsk = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.noise_volt = noise_volt = 0.0001
        self.freq_offset = freq_offset = 0
        self.eb = eb = 0.25
        self.arity = arity = 4
        self.SI_noise = SI_noise = 0.0001
        self.SI_channel_taps = SI_channel_taps = [1.0 + 0.0j, 1+0j]

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(0.999, 1.001, 0.0001, 1.00, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Timing Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 0,2,1,1)
        self._noise_volt_range = Range(0, 1, 0.01, 0.0001, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, 'Noise Voltage', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_volt_win, 0,0,1,1)
        self._freq_offset_range = Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Frequency Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 0,1,1,1)
        self._SI_noise_range = Range(0, 1, 0.01, 0.0001, 200)
        self._SI_noise_win = RangeWidget(self._SI_noise_range, self.set_SI_noise, 'SI_noise', "counter_slider", float)
        self.top_grid_layout.addWidget(self._SI_noise_win, 0,3,1,1)
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'Time: BW', "slider", float)
        self.top_grid_layout.addWidget(self._timing_loop_bw_win, 0,4,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['Signal1_rrc_rx_Real', 'Signal1_rrc_rx_Imag', 'SI_Signal2_rrc_rx_Real', 'SI_Signal2_rrc_rx_Imag', 'Sum_Real',
                  'Sum_Imag', 'Recovery_signal1_Real', 'Recovery_signal1_Imag', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["dark red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "Dark Blue", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*4):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.fir_filter_xxx_0_0_0 = filter.fir_filter_ccc(1, (rrc_rx))
        self.fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(1, (rrc_rx))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, (rrc_rx))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_modulator_0_0_0 = digital.generic_mod(
          constellation=qpsk,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
          constellation=qpsk,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=qpsk,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=False,
          log=False,
          )
        self.channels_channel_model_0_0_0 = channels.channel_model(
        	noise_voltage=noise_volt,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(SI_channel_taps),
        	noise_seed=0,
        	block_tags=False
        )
        self.channels_channel_model_0_0 = channels.channel_model(
        	noise_voltage=SI_noise,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(SI_channel_taps),
        	noise_seed=0,
        	block_tags=False
        )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_volt,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(taps),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b((100,200,101,202,150), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_b((1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,255), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((-1, ))
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 2))    
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_time_sink_x_0, 3))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_constellation_modulator_0, 0))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.digital_constellation_modulator_0_0, 0))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.digital_constellation_modulator_0_0_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.fir_filter_xxx_0, 0))    
        self.connect((self.channels_channel_model_0_0, 0), (self.fir_filter_xxx_0_0, 0))    
        self.connect((self.channels_channel_model_0_0_0, 0), (self.fir_filter_xxx_0_0_0, 0))    
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.channels_channel_model_0_0, 0))    
        self.connect((self.digital_constellation_modulator_0_0_0, 0), (self.channels_channel_model_0_0_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.fir_filter_xxx_0_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Recovery_principle")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_rx(firdes.root_raised_cosine(1.0, self.sps, 1, self.excess_bw, self.ntaps))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rrc_rx(firdes.root_raised_cosine(1.0, self.sps, 1, self.excess_bw, self.ntaps))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_rx(firdes.root_raised_cosine(1.0, self.sps, 1, self.excess_bw, self.ntaps))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0_0_0.set_timing_offset(self.time_offset)
        self.channels_channel_model_0_0.set_timing_offset(self.time_offset)
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps((self.taps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_rrc_rx(self):
        return self.rrc_rx

    def set_rrc_rx(self, rrc_rx):
        self.rrc_rx = rrc_rx
        self.fir_filter_xxx_0_0_0.set_taps((self.rrc_rx))
        self.fir_filter_xxx_0_0.set_taps((self.rrc_rx))
        self.fir_filter_xxx_0.set_taps((self.rrc_rx))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        self.channels_channel_model_0_0_0.set_noise_voltage(self.noise_volt)
        self.channels_channel_model_0.set_noise_voltage(self.noise_volt)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0_0_0.set_frequency_offset(self.freq_offset)
        self.channels_channel_model_0_0.set_frequency_offset(self.freq_offset)
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity

    def get_SI_noise(self):
        return self.SI_noise

    def set_SI_noise(self, SI_noise):
        self.SI_noise = SI_noise
        self.channels_channel_model_0_0.set_noise_voltage(self.SI_noise)

    def get_SI_channel_taps(self):
        return self.SI_channel_taps

    def set_SI_channel_taps(self, SI_channel_taps):
        self.SI_channel_taps = SI_channel_taps
        self.channels_channel_model_0_0_0.set_taps((self.SI_channel_taps))
        self.channels_channel_model_0_0.set_taps((self.SI_channel_taps))


def main(top_block_cls=Recovery_principle, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
