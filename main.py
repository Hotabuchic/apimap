from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.uic import loadUi
import requests


class MyWidget(QMainWindow):
    def __init__(self, ):
        super().__init__()
        loadUi('qt.ui', self)
        self.set_image()
        self.btn.clicked.connect(self.set_image)

    def set_image(self):
        l1, l2, spn = self.longitude.value(), self.latitude.value(), self.spn.value()
        req = requests.get(
            f"http://static-maps.yandex.ru/1.x/?ll={l1},{l2}&spn={spn},{spn}&l=map")
        file = open('temp.png', mode='wb')
        file.write(req.content)
        file.close()
        self.label.setPixmap(QPixmap('temp.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my = MyWidget()
    my.show()
    sys.exit(app.exec_())

