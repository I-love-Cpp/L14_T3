import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ul.ui', self)
        self.initUI()

    def initUI(self):
        self.flag = 0
        self.pushButton.clicked.connect(self.refresh)

    def refresh(self):
        self.flag = 1
        self.update()

    def paintEvent(self, e):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        count = randint(1, 10)
        for i in range(count):
            rad = randint(3, min(self.width(), self.height()) // 2)
            x = randint(rad, self.width() - rad)
            y = randint(rad, self.height() - rad)
            self.qp.setBrush(
                QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(x - rad, y - rad, 2 * rad, 2 * rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
