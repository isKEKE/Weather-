# _*_ coding: utf-8 _*_
from .CustomLable import CustomLable


class CompanyLable(CustomLable):
    '''单位'''
    def __init__(self, parent=None):
        super(CompanyLable, self).__init__(parent)


    def initLable(self) -> None:
        self.setObjectName("company")
        self.setGeometry(145, 137, 40, 40)
        self.setText("℃")
