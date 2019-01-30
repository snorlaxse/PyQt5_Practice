'''
@FileName: AutoCloseWindow.py
@Author: CaptainSE
@Time: 2019-01-28 
@Desc: 让程序定时关闭  QTimer.singleShot

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=140><b>Hello World，窗口在5秒后自动关闭!</b></font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)  # 闪屏 | 无框架窗口
    label.show()
    QTimer.singleShot(5000,app.quit)

    sys.exit(app.exec_())