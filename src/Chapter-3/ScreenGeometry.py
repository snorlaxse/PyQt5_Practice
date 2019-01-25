import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget


def onClick_Button():

    print("Method 1")
    print("widget.x() = %d" % widget.x())   # 250 (窗口横坐标)
    print("widget.y() = %d" % widget.y())   # 200（窗口纵坐标）
    print("widget.width() = %d" % widget.width())   # 300（工作区宽度）
    print("widget.height() = %d" % widget.height()) # 240（工作区高度）

    print("Method 2")
    print("widget.geometry().x() = %d" % widget.geometry().x())  # 250 (窗口横坐标)
    print("widget.geometry().y() = %d" % widget.geometry().y()) # 222（窗口纵坐标，不含标题栏）  # 标题栏的高度：22
    print("widget.geometry().width() = %d" % widget.geometry().width()) # 300（工作区宽度）
    print("widget.geometry().height() = %d" % widget.geometry().height()) # 240（工作区高度）

    print("Method 3")
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x()) # 250 (窗口横坐标)
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y()) # 200（窗口纵坐标）
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width()) # 300（工作区宽度）
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height()) # 262（工作区高度,含标题栏） # 标题栏的高度：22


app = QApplication(sys.argv)

widget = QWidget()

widget.resize(400,240)  # 240: 设置工作区的高度
widget.setWindowTitle('屏幕坐标系')

btn = QPushButton(widget)
btn.move(24,50)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

widget.show()

sys.exit(app.exec_())
