# -*- coding: utf-8 -*-
# DCM读取 (单文件单图 1*1显示)

import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import SimpleITK as sitk
import numpy as np
 
class dcmViewer(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("DcmViewer")  

        dcm_dir = '/Users/Captain/Downloads/Todo/dcom_sample'
        self.dcm_list = self.loadFiles(dcm_dir)
    
        layout = QVBoxLayout()
        self.m = PlotCanvas(self,width=5, height=4)
        layout.addWidget(self.m)

        self.scrollbar = QScrollBar(Qt.Horizontal)
        self.scrollbar.setMaximum(len(self.dcm_list))
        self.scrollbar.sliderMoved.connect(self.sliderMoved)
        layout.addWidget(self.scrollbar)
        
        self.setLayout(layout)
 
    def sliderMoved(self):
        print('当前值：%s' % self.sender().value())
        value = self.sender().value()
        
        print(self.dcm_list[value-1])
        self.dcmFile = self.dcm_list[value-1]
        self.m.plot(self.dcmFile)
        
    def loadFiles(self,file_dir):
        dcmlist=[] 
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.dcm':
                    dcmlist.append(os.path.join(root, file))
        dcmlist.sort()
        return dcmlist
        

class PlotCanvas(FigureCanvas):
 
    def __init__(self,parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

 
    def plot(self,dcmFile):
        self.fig.clear()

        image = sitk.ReadImage(dcmFile)
        image_array = np.squeeze(sitk.GetArrayFromImage(image))   # type(image_array) <class 'numpy.ndarray'>
        ax = self.figure.add_subplot(111)
        ax.imshow(image_array)
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = dcmViewer()
    example.show()
    sys.exit(app.exec_())