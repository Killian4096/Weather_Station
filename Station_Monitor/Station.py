#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt

from UART_Receiver import UART_Receiver
from GUI import Ui_MainWindow
import signal

from Temp_Plot import Temp_Plot

from UART_Decoder import ZMQ_UART_Connector



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    PlotWindow = Temp_Plot()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    tb = UART_Receiver()
    tb.start()

    tb._qtgui_freq_sink_x_0_win.setParent(ui.radioWidget)

    PlotWindow.setParent(ui.tempPlotWidget)


    MainWindow.show()

    ZUC = ZMQ_UART_Connector()

    buffer = 0

    while(True):
        ZUC.process_message()
        number = 0
        while number != None:
            buffer += 1
            number = ZUC.next_value()
            if number != None and buffer > 2:
                PlotWindow.log(number)
        PlotWindow.update_plot()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    def quitting():
        tb.stop()
        tb.wait()
        pass

    app.aboutToQuit.connect(quitting)
    app.exec_()

if __name__ == "__main__":
    main()