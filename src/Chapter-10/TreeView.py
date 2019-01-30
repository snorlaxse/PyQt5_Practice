'''
@FileName: TreeView.py
@Author: CaptainSE
@Time: 2019-01-28 
@Desc: QTreeView控件与系统定制模式

'''


import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)

    tree.setWindowTitle('QTreeView')
    tree.resize(600,400)
    tree.show()

    sys.exit(app.exec_())
