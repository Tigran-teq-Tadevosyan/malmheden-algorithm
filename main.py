from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QInputDialog, QWidget, QApplication, QTabWidget, QLabel, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QSpinBox, QVBoxLayout, QGroupBox, QGridLayout, QPushButton, QLineEdit, QFormLayout, QHBoxLayout, QLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDir, QObject, Qt, QThread, QTimer, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QGuiApplication, QCursor, QClipboard

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())