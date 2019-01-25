from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("noEchoLineEdit",noEchoLineEdit)
        formLayout.addRow("passwordLineEdit",passwordLineEdit)
        formLayout.addRow("passwordEchoOnEditLineEdit",passwordEchoOnEditLineEdit)

        # placeholdertext
        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('noEchoLineEdit')
        passwordLineEdit.setPlaceholderText('passwordLineEdit')
        passwordEchoOnEditLineEdit.setPlaceholderText('passwordEchoOnEditLineEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QLineEditEchoMode()
    main.show()

    sys.exit(app.exec_())