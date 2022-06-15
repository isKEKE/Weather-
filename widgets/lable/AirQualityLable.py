# _*_ coding: utf-8 _*_
from .CustomLable import CustomLable

class AirQualityLable(CustomLable):
    '''空气质量'''
    def __init__(self, parent=None):
        super(AirQualityLable, self).__init__(parent)


    def initLable(self) -> None:
        self.setObjectName("air")
        self.setGeometry(70, 225, 100, 20)
        super(AirQualityLable, self).initLable()