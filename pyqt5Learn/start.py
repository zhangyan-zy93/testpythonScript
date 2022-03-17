import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 此处直接展示helloworld
    # label = QLabel('hello world !')
    label = QLabel()
    label.setText('<font color = "red">Hello</font> <h1>World!</h1>')
    label.show()
    sys.exit(app.exec())