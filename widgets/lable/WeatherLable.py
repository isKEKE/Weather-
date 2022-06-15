# _*_ coding: utf-8 _*_
from .CustomLable import CustomLable

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets


class WeatherLable(CustomLable):
    '''天气标签'''
    def __init__(self, parent=None):
        super(WeatherLable, self).__init__(parent)


    def initLable(self) -> None:
        self.setObjectName("weather")
        self.setGeometry(145, 170, 40, 40)

        # 字体
        # fonts = QtWidgets.QFontDialog.getFont()
        # print(fonts[0].family(), fonts[0].styleName())
