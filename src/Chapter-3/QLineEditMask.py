from PyQt5.QtWidgets import *
import sys

class QLineEditMask(QWidget) :
    def __init__(self):
        super(QLineEditMask,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()
        # 192.168.21.45
        ipLineEdit.setInputMask('000.000.000.000;_')  # 未输入时默认为_
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_') # 未输入时默认为_
        dateLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#') # 未输入时默认为#

        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('Mac掩码', macLineEdit)
        formLayout.addRow('日期掩码',dateLineEdit)
        formLayout.addRow('许可证掩码',licenseLineEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()
    sys.exit(app.exec_())