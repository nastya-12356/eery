import sys
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint
from PyQt6 import uic
from Ui import Ui_Form


class Suprematism(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        self.x, self.y = -100, -100
        self.fig = 0
        self.setMouseTracking(True)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        size = randint(20, 100)
        self.x, self.y = randint(size, 400 - size), randint(size, 300 - size)
        color = QColor(randint(0,255), randint(0,255), randint(0,255))
        qp.setBrush(color)
        rect = QPointF(self.x, self.y)
        qp.drawEllipse(rect, size, size)


    def run(self):
        self.paint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())