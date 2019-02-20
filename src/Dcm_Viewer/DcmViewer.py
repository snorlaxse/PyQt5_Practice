# -*- coding: utf-8 -*-
# DCM读取 (多文件多图   n*n显示)

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

class dcmViewer(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle("DcmViewer")
        # dcm_dir = '/Users/shukai/Downloads/729427/A'
        dcm_dir1 = '/Users/Captain/Downloads/Todo/PATIENT_DICOM'
        dcm_dir2 = '/Users/Captain/Downloads/Todo/dcom_sample'
        dcm_dir3 = '/Users/Captain/Downloads/Todo/MASKS_DICOM/spleen'

        self.dcm_list1 = self.loadFiles(dcm_dir1)
        self.dcm_list2 = self.loadFiles(dcm_dir2)
        self.dcm_list3 = self.loadFiles(dcm_dir3)

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
        self.scrollbar1.setMaximum(len(self.dcm_list1))
        self.scrollbar1.sliderMoved.connect(lambda:self.sliderMoved("scrollbar1"))
        layout2.addWidget(self.scrollbar1)

        self.scrollbar2 = QScrollBar(Qt.Horizontal)
        self.scrollbar2.setMaximum(len(self.dcm_list2))
        self.scrollbar2.sliderMoved.connect(lambda:self.sliderMoved("scrollbar2"))
        layout2.addWidget(self.scrollbar2)

        self.scrollbar3 = QScrollBar(Qt.Horizontal)
        self.scrollbar3.setMaximum(len(self.dcm_list3))
        self.scrollbar3.sliderMoved.connect(lambda:self.sliderMoved("scrollbar3"))
        layout2.addWidget(self.scrollbar3)
        
        layout.addLayout(layout2)
        
        self.setLayout(layout)
 
    
    def sliderMoved(self,scrollbarName):
        if scrollbarName == 'scrollbar1':
            dcm_list = self.dcm_list1
        elif scrollbarName == 'scrollbar2':
            dcm_list = self.dcm_list2
        else:
             dcm_list = self.dcm_list3

        print('当前值：%s' % self.sender().value())
        print(dcm_list[self.sender().value()-1])
        dcmFile = dcm_list[self.sender().value()-1]
        
        if scrollbarName == 'scrollbar1':
            self.plotCanvas1.plot(dcmFile)
        elif scrollbarName == 'scrollbar2':
            self.plotCanvas2.plot(dcmFile)
        else:
            self.plotCanvas3.plot(dcmFile)

    def loadFiles(self,file_dir):
        dcmlist=[] 
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                # if os.path.splitext(file)[1] == '.dcm':
                #     dcmlist.append(os.path.join(root, file))
                dcmlist.append(os.path.join(root, file))

        dcmlist.sort()
        return dcmlist

class PlotCanvas(FigureCanvas):
    def __init__(self,parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_facecolor('black')
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
    def plot(self,dcmFile):
        self.fig.clear()
        image = sitk.ReadImage(dcmFile)   # type(image) <class 'SimpleITK.SimpleITK.Image'>
        image_array = np.squeeze(sitk.GetArrayFromImage(image))   # type(image_array)  <class 'numpy.ndarray'>   # image_array.shape (512, 512)
        ax = self.figure.add_subplot(111)
        ax.imshow(image_array,cmap='gray')
        ax.axis('off')
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    example = dcmViewer()
    example.show()
    sys.exit(app.exec_())