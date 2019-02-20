# -*- coding: utf-8 -*-
# DCM读取 (单文件多视角   1*n显示)

import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import SimpleITK as sitk
import numpy as np
import qdarkstyle
import scipy.misc


class dcmViewer(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("DcmViewer_3d")

        # dcm_dir = '/Users/shukai/Downloads/729427/A'
        dcm_dir = '/Users/Captain/Downloads/Todo/dcom_sample'
        
        self.dcm_list = self.loadFiles(dcm_dir)
        self.dcm_ndarrays = self.to_3d_array(self.dcm_list) # 读取所有文件 （二维 -> 三维）

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        self.plotCanvas1 = PlotCanvas(self,width=5, height=4)
        self.plotCanvas2 = PlotCanvas(self,width=5, height=4)
        self.plotCanvas3 = PlotCanvas(self,width=5, height=4)
        layout1.addWidget(self.plotCanvas1)
        layout1.addWidget(self.plotCanvas2)
        layout1.addWidget(self.plotCanvas3)
        layout.addLayout(layout1)

        layout2 = QHBoxLayout()
        self.scrollbar1 = QScrollBar(Qt.Horizontal)
        self.scrollbar1.setMaximum(len(self.dcm_list))
        self.scrollbar1.sliderMoved.connect(lambda:self.sliderMoved("scrollbar1"))
        layout2.addWidget(self.scrollbar1)

        self.scrollbar2 = QScrollBar(Qt.Horizontal)
        self.scrollbar2.setMaximum(len(self.dcm_list))
        self.scrollbar2.sliderMoved.connect(lambda:self.sliderMoved("scrollbar2"))
        layout2.addWidget(self.scrollbar2)

        self.scrollbar3 = QScrollBar(Qt.Horizontal)
        self.scrollbar3.setMaximum(len(self.dcm_list))
        self.scrollbar3.sliderMoved.connect(lambda:self.sliderMoved("scrollbar3"))
        layout2.addWidget(self.scrollbar3)
        
        layout.addLayout(layout2)
        
        self.setLayout(layout)
 
    
    def sliderMoved(self,scrollbarName):

        print('当前值：%s' % self.sender().value())
        value = self.sender().value()

        if scrollbarName == 'scrollbar1':
            self.plotCanvas1.plot3s(scrollbarName,self.dcm_ndarrays,value-1)
        elif scrollbarName == 'scrollbar2':
            self.plotCanvas2.plot3s(scrollbarName,self.dcm_ndarrays,value-1)
        else:
            self.plotCanvas3.plot3s(scrollbarName,self.dcm_ndarrays,value-1)


    def loadFiles(self,file_dir):
        dcmlist=[] 
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                dcmlist.append(os.path.join(root, file))

        dcmlist.sort()
        return dcmlist

    def to_3d_array(self,dcm_list):
        to_3d_list = []
        i = 0
        for dcmFile in dcm_list:
            image = sitk.ReadImage(dcmFile)
            image_array = np.squeeze(sitk.GetArrayFromImage(image)) 
            
            if i == 0: 
                i += 1
                to_3d_list = [image_array]
            else:
                to_3d_list.append(image_array)

        to_3d_ndarray = np.array(to_3d_list)    # to_3d_ndarray.shape (245, 512, 512)

        return to_3d_ndarray

class PlotCanvas(FigureCanvas):
    def __init__(self,parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_facecolor('black')
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
    def plot3s(self,scrollbarName,dcm_ndarrays,value):  

        self.fig.clear()
        ax = self.figure.add_subplot(111)

        # 依据scrollbar.value值，调整某一维の数值
        if scrollbarName == 'scrollbar1':
            gray = dcm_ndarrays[value]
            gray = scipy.misc.imresize(gray,(200,200))
            
        elif scrollbarName == 'scrollbar2':
            gray = dcm_ndarrays[:,value,:]
            gray = scipy.misc.imresize(gray,(200,200))

        else:
            gray = dcm_ndarrays[:,:,value]
            gray = scipy.misc.imresize(gray,(200,200))

        ax.imshow(gray,cmap='gray')

        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    example = dcmViewer()
    example.show()
    sys.exit(app.exec_())