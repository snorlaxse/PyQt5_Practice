'''
@FileName: PyFactorial.py
@Author: CaptainSE
@Time: 2019-01-31 
@Desc: 

'''

'''

JavaScript调用Python函数计算阶乘

将Python的一个对象映射到JavaScript中

将槽函数映射到JavaScript中

'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import  QWebChannel
from factorial import *
import sys,os

channel = QWebChannel()
factorial = Factorial()
class PyFactorial(QWidget):

    def __init__(self):
        super(PyFactorial, self).__init__()
        self.setWindowTitle('Python计算阶乘')
        self.resize(600,300)
        layout=QVBoxLayout()

        self.browser = QWebEngineView()
        url = os.getcwd() + '/f.html'
        self.browser.load(QUrl.fromLocalFile(url))
        channel.registerObject("obj",factorial)
        self.browser.page().setWebChannel(channel)

        layout.addWidget(self.browser)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyFactorial()
    win.show()
    sys.exit(app.exec_())
