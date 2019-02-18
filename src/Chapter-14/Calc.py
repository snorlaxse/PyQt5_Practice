'''
@FileName: Calc.py
@Author: CaptainSE
@Time: 2019-01-31 
@Desc: 栅格布局：实现计算器UI

'''

import sys
from PyQt5.QtWidgets import *


class Calc(QWidget) :
    def __init__(self):
        super(Calc,self).__init__()
        self.setWindowTitle("栅格布局")

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls','Back','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']

        positions = [(i,j) for i in range(5) for j in range(4)]
        # print(positions)
        # [ (0, 0), (0, 1), (0, 2), (0, 3),
        #   (1, 0), (1, 1), (1, 2), (1, 3),
        #   (2, 0), (2, 1), (2, 2), (2, 3),
        #   (3, 0), (3, 1), (3, 2), (3, 3),
        #   (4, 0), (4, 1), (4, 2), (4, 3)]


        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            # print(position)
            grid.addWidget(button,*position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())