'''
@FileName: PrintSupport.py
@Author: CaptainSE
@Time: 2019-01-27 
@Desc: 使用打印机

'''

from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *
import sys

class PrintSupport(QMainWindow):
    def __init__(self):

        super(PrintSupport,self).__init__()
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton('打印QTextEdit控件中的内容',self)
        self.button.setGeometry(20,20,260,30)

        self.editor = QTextEdit('默认文本',self)
        self.editor.setGeometry(20,60,260,200)

        self.button.clicked.connect(self.print)

    def print(self):

        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()

        # 将绘制的目标重定向(begin)到打印机(printer)
        painter.begin(printer)
        screen = self.editor.grab()  # 获取屏幕
        painter.drawPixmap(10,10,screen) # 内容以图片形式打印
        painter.end()
        print("print")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PrintSupport()
    gui.show()
    app.exec_()