# _*_ coding: utf-8 _*_
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class CustomLable(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(CustomLable, self).__init__(parent)
        self.initLable()


    def initLable(self) -> None:
        '''初始化标签'''
        # 文本居中
        self.setAlignment(Qt.AlignCenter)
        pass