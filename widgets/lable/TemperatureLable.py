# _*_ config: utf-8 _*_
from PyQt5.QtCore import Qt
from .CustomLable import CustomLable


class TemperatureLable(CustomLable):
    '''温度标签'''
    def __init__(self, parent=None):
        super(TemperatureLable, self).__init__(parent)


    def initLable(self) -> None:
        self.setObjectName("temperature")
        self.setGeometry(70, 140, 75, 65)
        super(TemperatureLable, self).initLable()

