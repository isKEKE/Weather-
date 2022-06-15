# _*_ coding: utf-8 _*_
from .CustomLable import CustomLable


class TitleLable(CustomLable):
    '''标题'''
    def __init__(self, parent=None):
        super(TitleLable, self).__init__(parent)


    def initLable(self) -> None:
        self.setObjectName("title")
        self.setGeometry(10, 3, 200, 20)
