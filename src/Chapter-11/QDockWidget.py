'''
@FileName: QDockWidget.py
@Author: CaptainSE
@Time: 2019-01-28 
@Desc: 停靠控件（QDockWidget）

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)

        self.setWindowTitle("停靠控件（QDockWidget）")
        self.setCentralWidget(QLineEdit())

        layout = QHBoxLayout()

        self.items = QDockWidget('Dockable',self)

        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        self.items.setWidget(self.listWidget)

        self.items.setFloating(True) # 初始时为浮动状态

        self.addDockWidget(Qt.RightDockWidgetArea,self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())
