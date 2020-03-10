from PyQt5.Qt import *

from PyQt5.Qt import *
import sys
import os

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,200)
        self.setWindowTitle('主神空间')
        self.set_widget()
        self.setFixedSize(500,200)

    def set_widget(self):
        label = QLabel('想明白生命的意义吗？想真正的......活着吗？',self)
        label.resize(100,100)
        label.adjustSize()
        window_width = self.width()
        window_height = self.height()
        label.move((window_width-label.width())/2,(window_height-label.height()-50)/2)

        button1 = QPushButton('YES',self)
        button2 = QPushButton('NO',self)
        button1.move((window_width-button1.width()-200)/2,(window_height-button1.height()+50)/2)
        button2.move((window_width-button2.width()+200)/2,(window_height-button2.height()+50)/2)

        button2.clicked.connect(self.close)
        button1.clicked.connect(self.shutdown)

    def shutdown(self):
        os.system('shutdown -s -t 0')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_widget = MyWidget()

    my_widget.show()

    sys.exit(app.exec_())


