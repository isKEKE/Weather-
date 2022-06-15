# _*_coding: utf-8 _*_
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from .CustomLable import CustomLable

class WeatherImageLable(CustomLable):
    '''天气图片'''
    _pixmap = None
    _size = None

    _width = 100
    _height = 100
    def __init__(self, parent=None):
        super(WeatherImageLable, self).__init__(parent)


    def initLable(self) -> None:
        self.setObjectName("image")
        self.setGeometry(70, 40, self._width, self._height)
        super(WeatherImageLable, self).initLable()


    def setImage(self, img: str) -> None:
        '''设置标签图片, 自适应大小'''
        self._size = QtCore.QSize(self._width, self._height)
        self._pixmap = QtGui.QPixmap(img)
        self._pixmap.scaled(self._size, Qt.KeepAspectRatio)
        self.setPixmap(self._pixmap)
        self.setScaledContents(True)
        