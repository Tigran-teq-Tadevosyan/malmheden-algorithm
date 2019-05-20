from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys

import SampleBdryFuncs
import computer

def calculateForPlot(x,y,radius,bdryIndex):
    bdry = SampleBdryFuncs.bdry_funcs[bdryIndex]
    return computer.compute( x,y,radius,bdry )

class Visualizer(object):
    def __init__(self,raduis,bdryIndex):
        self.traces = dict()
        # self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 40
        self.w.setWindowTitle('pyqtgraph example: GLLinePlotItem')
        self.w.setGeometry(0, 110, 1920, 1080)
        self.w.show()

        # create the background grids
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.w.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.w.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.w.addItem(gz)

        self.radius = raduis
        self.bdryIndex = bdryIndex
        self.count = 100
        self.space = self.radius/(np.sqrt(2)*2)
        self.x = np.linspace(-self.space, self.space, self.count)
        self.y = np.linspace(-self.space, self.space, self.count)

        for i in range(self.count):
            Current_y = np.sqrt(self.radius**2 - self.x[i]**2)
            yi = np.array([self.y[i]] * self.count)
            test_yi = np.array([Current_y] * self.count)
            # z = testFunction(self.x, yi)
            z = []
            for index in range(len(self.x)):
                z.append( calculateForPlot(self.x[index], yi[index], self.radius, self.bdryIndex) )
            pts = np.vstack([self.x, yi , z]).transpose()
            if i%5 == 0:
                print(pts)
                # print("yi",yi[0])
                # print("x",self.x[i])
                # print("test_yi",test_yi[0])
            self.traces[i] = gl.GLLinePlotItem(pos=pts, color=pg.glColor(
                (i, self.count * 1.6)), width=(i + 1) / 10, antialias=True)
            self.w.addItem(self.traces[i])

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()


# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    v = Visualizer()
    v.start()