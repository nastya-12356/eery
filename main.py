class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.x, self.y = -100, -100
        self.fig = 3
        self.setMouseTracking(True)
