'''
@FileName: SignalSlotDemo.py
@Author: CaptainSE
@Time: 2019-01-31 
@Desc: 信号（Signal）与槽（Slot）

'''

from PyQt5.QtWidgets import *
import sys

class SigalSlotDemo(QWidget):
    def __init__(self):
        super(SigalSlotDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('信号（Signal）与槽（Slot）')
        self.btn = QPushButton('我的按钮',self)
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        self.btn.setText("信号已经发出")
        self.btn.setStyleSheet("QPushButton(max-width:100px;min-width:100px")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SigalSlotDemo()
    gui.show()
    sys.exit(app.exec_())