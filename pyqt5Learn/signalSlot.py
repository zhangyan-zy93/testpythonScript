import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Demo(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super(Demo, self).__init__()
        # self.button = QPushButton('Start', self)
        # 此处的标准写法就是 widget.signal.connect(slot)；
        # self.button.pressed.connect(self.change_text)
        # self.button.pressed.connect(self.button.released)
        # self.button.released.connect(self.change_text)
        self.label = QLabel('Hello World', self)
        self.my_signal.connect(self.change_label_text)

    def change_text(self):
            print('change text')
            if self.button.text() == 'Start':
                self.button.setText('stop')
                # self.button.clicked.disconnect(self.change_text)  解绑signal和slot
            else:
                self.button.setText('Start')
                # self.button.clicked.disconnect(self.change_text)

    def change_label_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    def mousePressEvent(self,QMouseEvent):
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec())
