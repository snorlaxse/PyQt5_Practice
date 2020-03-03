# -*- coding: utf-8 -*-
# nii读取 (单文件多视角   1*n显示)

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


class PETViewer(QWidget):
 
    def __init__(self, nii_file):
        super().__init__()

        nii_image = sitk.ReadImage(nii_file)
        self.nii_arr = sitk.GetArrayFromImage(nii_image)
        print(self.nii_arr.shape)

        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("PETViewer")
        
        layout = QHBoxLayout()

        layout1 = QVBoxLayout()
        self.plotCanvas1 = PlotCanvas(self, width=5, height=4)
        self.scrollbar1 = QScrollBar(Qt.Horizontal)
        self.scrollbar1.setMaximum(self.nii_arr.shape[0])
        self.scrollbar1.sliderMoved.connect(lambda:self.sliderMoved("scrollbar1"))
        layout1.addWidget(self.plotCanvas1)
        layout1.addWidget(self.scrollbar1)

        layout2 = QVBoxLayout()
        self.plotCanvas2 = PlotCanvas(self, width=5, height=4)
        self.scrollbar2 = QScrollBar(Qt.Horizontal)
        self.scrollbar2.setMaximum(self.nii_arr.shape[1])   
        self.scrollbar2.sliderMoved.connect(lambda:self.sliderMoved("scrollbar2"))
        layout2.addWidget(self.plotCanvas2)
        layout2.addWidget(self.scrollbar2)        

        layout3 = QVBoxLayout()
        self.scrollbar3 = QScrollBar(Qt.Horizontal)
        self.scrollbar3.setMaximum(self.nii_arr.shape[2])
        self.scrollbar3.sliderMoved.connect(lambda:self.sliderMoved("scrollbar3"))
        self.plotCanvas3 = PlotCanvas(self, width=5, height=4)
        layout3.addWidget(self.plotCanvas3)
        layout3.addWidget(self.scrollbar3)

        layout.addLayout(layout1)        
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        self.setLayout(layout)
 
    
    def sliderMoved(self,scrollbarName):

        print('当前值：%s' % self.sender().value())
        value = self.sender().value()

        if scrollbarName == 'scrollbar1':
            self.plotCanvas1.plot3s(scrollbarName,self.nii_arr,value)
        elif scrollbarName == 'scrollbar2':
            self.plotCanvas2.plot3s(scrollbarName,self.nii_arr,value)
        elif scrollbarName == 'scrollbar3':
            self.plotCanvas3.plot3s(scrollbarName,self.nii_arr,value)
        else:
            print("{} not support.".format(scrollbarName))
            pass


class PlotCanvas(FigureCanvas):

    def __init__(self,parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_facecolor('black')
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
    def plot3s(self,scrollbarName,nii_arr,value):  

        self.fig.clear()
        ax = self.figure.add_subplot(111)

        # 依据scrollbar.value值，调整某一维の数值        
        if scrollbarName == 'scrollbar1':
            slice = nii_arr[value-1,:,:]
            
        elif scrollbarName == 'scrollbar2':
            slice = nii_arr[:, value-1, :]
            slice = slice[::-1]  # 上下翻转180°

        elif scrollbarName == 'scrollbar3':
            slice = nii_arr[:, :, value-1]
            slice = slice[::-1]  # 上下翻转180°

        else:
            print("{} not support.".format(scrollbarName))
            pass

        ax.imshow(slice,cmap='jet')
        # ax.imshow(slice,cmap='rainbow')

        self.draw()

if __name__ == '__main__':

    nii_file = './AD_55_094_S_1397_20070625_UR.nii'
    nii_file = './MCI_56_123_S_4806_20120724_UR.nii'
    nii_file = './CN_56_168_S_6085_20171201_UR.nii'
    nii_file = './MCI_56_123_S_4806_20120626_N3_MNI_ht_norm.nii.gz'
    
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    example = PETViewer(nii_file)
    example.show()
    sys.exit(app.exec_())