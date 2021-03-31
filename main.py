import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('qt.ui', self)
        self.key = "40d1649f-0493-4b70-98ba-98533de7710b"
        self.set_image()
        self.btn.clicked.connect(self.set_image)
        self.cancel.clicked.connect(self.cancel_search)

    def set_image(self):
        response = requests.get(
            f"http://geocode-maps.yandex.ru/1.x/?apikey={self.key}&geocode={self.search.text()}&format=json").json()
        toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        self.l1, self.l2 = toponym["Point"]["pos"].split()
        self.spn = self.spnn.value()
        self.mapp = "map"
        if self.mappp.currentText() == "Спутник":
            self.mapp = "sat"
        elif self.mappp.currentText() == "Гибрид":
            self.mapp = "sat,skl"
        req = requests.get(
            f"http://static-maps.yandex.ru/1.x/?ll={self.l1},{self.l2}&"
            f"spn={self.spn},{self.spn}&l={self.mapp}&pt={self.l1},{self.l2},org")
        file = open('temp.png', mode='wb')
        file.write(req.content)
        file.close()
        self.label.setPixmap(QPixmap('temp.png'))

    def cancel_search(self):
        req = requests.get(
            f"http://static-maps.yandex.ru/1.x/?ll={self.l1},{self.l2}&"
            f"spn={self.spn},{self.spn}&l={self.mapp}")
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
