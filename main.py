import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('qt.ui', self)
        self.set_image()
        self.btn.clicked.connect(self.set_image)

    def set_image(self):
        l1, l2, spn = self.longitude.value(), self.latitude.value(), self.spn.value()
        mapp = "map"
        if self.mapp.currentText() == "Спутник":
            mapp = "sat"
        elif self.mapp.currentText() == "Гибрид":
            mapp = "sat,skl"
        req = requests.get(
            f"http://static-maps.yandex.ru/1.x/?ll={l1},{l2}&spn={spn},{spn}&l={mapp}")
        file = open('temp.png', mode='wb')
        file.write(req.content)
        file.close()
        self.label.setPixmap(QPixmap('temp.png'))

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_PageUp:
    #         self.spn.setValue(self.spn.value() + 0.04)
    #         self.set_image()
    #     elif event.key() == Qt.Key_PageDown:
    #         self.spn.setValue(self.spn.value() - 0.04)
    #         self.set_image()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my = MyWidget()
    my.show()
    sys.exit(app.exec_())
