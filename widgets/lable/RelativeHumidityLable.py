# _*_ coding: utf-8 _*_
from .CustomLable import CustomLable


class RelativeHumidityLable(CustomLable):
    '''相对湿度'''
    def __init__(self, parent=None):
        super(RelativeHumidityLable, self).__init__(parent)
    
    
    def initLable(self) -> None:
        self.setObjectName("humidity")
        self.setGeometry(70, 255, 100, 20)
        super(RelativeHumidityLable, self).initLable()
