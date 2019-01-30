'''

创建和使用菜单

'''

import sys
from PyQt5.QtWidgets import *

class Menu(QMainWindow) :
    def __init__(self):
        super(Menu,self).__init__()
        bar = self.menuBar()  # 获取菜单栏

        file = bar.addMenu("文件")
        file.addAction("新建")

        save = QAction("保存",self)
        save.setShortcut("Ctrl + S")
        save.triggered.connect(self.process)
        file.addAction(save)

        quit = QAction("退出",self)
        file.addAction(quit)

        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

    def process(self,a):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())