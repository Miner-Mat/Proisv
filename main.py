import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # загружаем дизайн
        self.initUI()
        self.paint = False

    def initUI(self):
        self.pushButton.clicked.connect(self.activate_paint)  # привязываем кнопку

    def activate_paint(self):
        self.paint = True  # изменяем сотояние на 'рисование активно'
        self.update()  # принудительно вызываем paintEvent

    def paintEvent(self, e):  # переопределение метода paintEvent
        if self.paint:  # проверяем, нужно ли рисовать
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()

    def run(self, qp):
        # Рисуем круги желтого цвета с случайным диаметром
        qp.setBrush(QBrush(QColor(219, 242, 7)))
        qp.drawEllipse(500, 50, random.randint(100, 250), random.randint(100, 250))
        qp.drawEllipse(300, 100, random.randint(100, 250), random.randint(100, 250))
        qp.drawEllipse(150, 150, random.randint(100, 250), random.randint(100, 250))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
