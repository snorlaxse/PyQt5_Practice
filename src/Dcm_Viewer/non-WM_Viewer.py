# -*- coding: utf-8 -*-
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
import pdb


class PETViewer(QWidget):
 
    def __init__(self, pet_file, mri_file, wm_file):
        super().__init__()
        
        pet_image = sitk.ReadImage(pet_file)
        mri_image = sitk.ReadImage(mri_file)
        wm_image = sitk.ReadImage(wm_file)

        self.pet_arr = sitk.GetArrayFromImage(pet_image)
        self.mri_arr = sitk.GetArrayFromImage(mri_image)
        self.wm_arr = sitk.GetArrayFromImage(wm_image)

        # rm
        remove_ixs=np.where(self.wm_arr>0.1*np.max(self.wm_arr))
        # remove_ixs_x, remove_ixs_y, remove_ixs_z = remove_ixs[0], remove_ixs[1], remove_ixs[2]
        # pdb.set_trace()
        self.rm_arr = sitk.GetArrayFromImage(pet_image)
        self.rm_arr[remove_ixs] = 0

        print(self.pet_arr.shape)
        print(self.mri_arr.shape)
        print(self.wm_arr.shape)
        print(self.rm_arr.shape)

        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("Non-WM Viewer")
        
        layout1 = QHBoxLayout()
        self.plotCanvas1 = PlotCanvas(self, width=2, height=2)
        self.plotCanvas2 = PlotCanvas(self, width=2, height=2)
        self.plotCanvas3 = PlotCanvas(self, width=2, height=2)
        self.plotCanvas4 = PlotCanvas(self, width=2, height=2)
        layout1.addWidget(self.plotCanvas1)
        layout1.addWidget(self.plotCanvas2)
        layout1.addWidget(self.plotCanvas3)
        layout1.addWidget(self.plotCanvas4)

        layout2 = QHBoxLayout()
        self.scrollbar = QScrollBar(Qt.Horizontal)
        self.scrollbar.setMaximum(self.pet_arr.shape[0])
        self.scrollbar.sliderMoved.connect(lambda:self.sliderMoved("scrollbar"))
        layout2.addWidget(self.scrollbar)        

        layout = QVBoxLayout()
        pdb.set_trace()
        layout.addLayout(layout1)        
        layout.addLayout(layout2)
        self.setLayout(layout)
 
    
    def sliderMoved(self,scrollbarName):

        print('当前值：%s' % self.sender().value())
        value = self.sender().value()

        self.plotCanvas1.plot(self.pet_arr, value, cmap='jet')
        self.plotCanvas2.plot(self.mri_arr, value, cmap='gray')
        self.plotCanvas3.plot(self.wm_arr, value, cmap='gray')
        self.plotCanvas4.plot(self.rm_arr, value, cmap='jet')


class PlotCanvas(FigureCanvas):

    def __init__(self,parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_facecolor('black')
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    def plot(self,nii_arr,value,cmap='jet'):  
        self.fig.clear()
        ax = self.figure.add_subplot(111)

        # 依据scrollbar.value值，调整某一维の数值        
        slice = nii_arr[value-1,:,:]

        ax.imshow(slice,cmap=cmap)

        self.draw()

if __name__ == '__main__':

    pet_file = './MCI_56_123_S_4806_20120724_UR_N3.nii.gz'
    mri_file = 'MCI_56_123_S_4806_20120626_N3_MNI_ht_norm.nii.gz'
    wm_file = './MCI_56_123_S_4806_20120626_N3_MNI_ht_norm_FAST/MCI_56_123_S_4806_20120626_N3_MNI_ht_norm_pve_2.nii.gz'
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    example = PETViewer(pet_file, mri_file, wm_file)
    example.show()
    sys.exit(app.exec_())