import sys
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint
from math import sin, cos, pi


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.x, self.y = -100, -100
        self.fig = 3
        self.setMouseTracking(True)
