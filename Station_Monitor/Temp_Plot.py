import matplotlib.pyplot as plt
import numpy as np
from UART_Decoder import ZMQ_UART_Connector

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import time

import math

class Temp_Plot(FigureCanvasQTAgg):
    def __init__(self, width=8.04, height=2.51, dpi=100):
        plt.ion()
        self.figure = plt.figure(figsize=(width, height), dpi=dpi)
        super(Temp_Plot, self).__init__(self.figure)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_autoscale_on(True)
        self.axes.autoscale_view(True,True,True)

        self.data_log = np.array([])
        self.x_log = np.array([])
        self.plot, = plt.plot([], [], 'r-')
        plt.xlabel("Sample")
        plt.ylabel("Temp (C)")
        plt.draw()

    def log(self, data_point):
        self.data_log = np.append(self.data_log, data_point)
        self.x_log = np.append(self.x_log, len(self.x_log))
        self.update_plot()

    def update_plot(self):
        self.plot.set_data(self.x_log, self.data_log)
        self.axes.relim()
        self.axes.autoscale_view(True,True,True)
        plt.draw()
        self.figure.canvas.flush_events()

'''def main():
    ZUC = ZMQ_UART_Connector()
    TP = Temp_Plot()
    while True:
        #ZUC.process_message()
        while True:
            #number = ZUC.next_value()
            #if number == None:
            #    break
            #TP.log(number)
            TP.log(3)
            TP.update_plot()
            break


if __name__ == "__main__":
    main()'''
