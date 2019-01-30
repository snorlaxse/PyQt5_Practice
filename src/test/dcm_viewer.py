'''
@FileName: dcm_viewer.py.py
@Author: CaptainSE
@Time: 2019-01-28 
@Desc: 

'''

import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import SimpleITK as sitk
import numpy as np

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        dcm_dir = '/Users/Captain/Desktop/A_dcm/'
        self.dcm_list = self.loadFiles(dcm_dir)

        self.setWindowTitle('滑块控件演示')
        self.resize(700, 700)

        layout = QVBoxLayout()
        self.label = QLabel('你好 PyQt5')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)
        layout.addWidget(self.slider)
        # 设置最小值
        self.slider.setMinimum(1)
        # 设置最大值
        self.slider.setMaximum(len(self.dcm_list))
        # 步长
        self.slider.setSingleStep(1)
        # 设置当前值
        self.slider.setValue(1)
        # 设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        # self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.valueChange)

        self.setLayout(layout)

    def valueChange(self):
        print('当前值：%s' % self.sender().value())
        value = self.sender().value()
        # value值映射至要显示的文件名, display
        print(self.dcm_list[value - 1])
        self.label.setPixmap(QPixmap(self.dcm2Qimg(self.dcm_list[value - 1])))

    def loadFiles(self, file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.dcm':
                    L.append(os.path.join(root, file))
        L.sort()
        return L

    def dcm2Qimg(self, dcmFile):
        image = sitk.ReadImage(dcmFile)
        image_array = np.squeeze(sitk.GetArrayFromImage(image))

        # image_array = np.transpose(image_array,(1,0,2)).copy()

        # QImage(uchar * data, int width, int height, int bytesPerLine, Format format) 中的
        # bytesPerLine 参数不能省略,负责造成Qimage数据错误,显示图片不正常,此参数设置为image的width*image.channels
        qimage = QImage(image_array, image_array.shape[1], image_array.shape[0], image_array.shape[1] * 3,
                        QImage.Format_RGB888)
        print(qimage)
        return qimage


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())