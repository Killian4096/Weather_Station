#!/usr/bin/env python3
from PyQt5 import Qt, QtWidgets
import signal

from GUI import Ui_MainWindow
from UART_Receiver import UART_Receiver

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    Freq_Graph = UART_Receiver()
    Freq_Graph.setParent(ui.radioWidget)
    Freq_Graph.setGeometry(ui.radioWidget.geometry())

    Freq_Graph.start()

    MainWindow.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)
    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        Freq_Graph.stop()
        Freq_Graph.wait()

    app.aboutToQuit.connect(quitting)
    app.exec_()