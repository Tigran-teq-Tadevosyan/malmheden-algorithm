from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QInputDialog, QWidget, QApplication, QTabWidget, QLabel, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QSpinBox, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLineEdit, QFormLayout, QHBoxLayout, QLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDir, QObject, Qt, QThread, QTimer, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QGuiApplication, QCursor, QClipboard

import numpy as np
import pyqtgraph as pg


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()


import sys

import MainWindowUI
import SampleBdryFuncs
import computer

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = MainWindowUI.Ui_MainWindow()
        self.ui.setupUi(self)
    
    @pyqtSlot()
    def calculateValue(self):
        radius = self.ui.radiusInput.value()
        bdry = SampleBdryFuncs.bdry_funcs[self.ui.bdryFunctionInput.currentIndex()]
        a = self.ui.aInput.value()
        b = self.ui.bInput.value()
        self.ui.functionOutputLabel.setText( str( computer.compute( a,b,radius,bdry ) ) )

    @pyqtSlot()
    def plot(self):
        radius = self.ui.radiusInput.value()
        bdry = SampleBdryFuncs.bdry_funcs[self.ui.bdryFunctionInput.currentIndex()]
        range_data = []
        data = []
        fixed_x = self.ui.plottingXInput.value()
        fixed_y = self.ui.plottingYInput.value()
        if self.ui.plottingOptionInput.currentIndex() == 0:
            for index in range(-radius,radius+1):
                range_data.append(index)
                data.append(computer.compute( fixed_x,index,radius,bdry ))
        else:
            for index in range(-radius,radius+1):
                range_data.append(index)
                data.append(computer.compute( index,fixed_y,radius,bdry ))
        pg.plot(range_data,data, title="Graph")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())